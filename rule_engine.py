import re

# 1. Define the Data Structure for AST
class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.type = node_type # "operator" or "operand"
        self.left = left # left child (another Node)
        self.right = right # right child (another Node)
        self.value = value # condition or operator, e.g., "age > 30"


# 2. API Design

# a) Create Rule
def create_rule(rule_string):
    # Break the rule string into conditions and operators
    tokens = re.split(r'(\sAND\s|\sOR\s)', rule_string) # Splits on AND/OR operators

    def build_ast(tokens):
        # Base case: a single condition (operand)
        if len(tokens) == 1:  
            return Node("operand", value=tokens[0].strip())

        # Recursive case: Combine operator and operands
        operator = tokens[1].strip() # AND/OR operator
        left_operand = tokens[0].strip()
        right_operand = tokens[2].strip()

        left_node = Node("operand", value=left_operand)
        right_node = Node("operand", value=right_operand)

        return Node("operator", left=left_node, right=right_node, value=operator)

    return build_ast(tokens)


# b) Combine Rules
def combine_rules(rule_strings):
    combined_ast = None
    for rule_string in rule_strings:
        rule_ast = create_rule(rule_string)
        if combined_ast is None:
            combined_ast = rule_ast
        else:
            # Combine with AND for now (can be parameterized)
            combined_ast = Node("operator", left=combined_ast, right=rule_ast, value="AND")
    return combined_ast


# c) Evaluate Rule
def evaluate_rule(ast, data):
    if ast.type == "operand":
        return eval_condition(ast.value, data)
    elif ast.type == "operator":
        if ast.value == "AND":
            return evaluate_rule(ast.left, data) and evaluate_rule(ast.right, data)
        elif ast.value == "OR":
            return evaluate_rule(ast.left, data) or evaluate_rule(ast.right, data)


def eval_condition(condition, data):
    # Validate the condition format
    try:
        field, operator, value = re.split(r'\s(>|<|=)\s', condition)
        field_value = data.get(field)

        # Handle cases where the field might not exist
        if field_value is None:
            raise ValueError(f"Field '{field}' is not present in the data.")

        # Handle the comparison based on operator
        if operator == ">":
            return field_value > int(value)
        elif operator == "<":
            return field_value < int(value)
        elif operator == "=":
            return field_value == value.strip("'")
        else:
            raise ValueError(f"Unsupported operator '{operator}' in condition '{condition}'.")

    except Exception as e:
        raise ValueError(f"Error evaluating condition '{condition}': {str(e)}")


# 3. Sample Test Cases
def main():
    try:
        print("Creating rule...")
        rule_string = "age > 30 AND department = 'Sales'"
        rule_ast = create_rule(rule_string)
        print("AST for rule created successfully.")

        print("Combining rules...")
        rules = [
            "age > 30 AND department = 'Sales'",
            "age < 25 AND department = 'Marketing'"
        ]
        combined_ast = combine_rules(rules)
        print("Combined AST created successfully.")

        print("Evaluating rule...")
        data = {"age": 35, "department": "Sales", "salary": 60000}
        result = evaluate_rule(rule_ast, data) # Should return True
        print("Evaluation result:", result)

        print("Evaluating combined rules...")
        combined_data = {"age": 22, "department": "Marketing"}
        combined_result = evaluate_rule(combined_ast, combined_data) # Should return False
        print("Combined evaluation result:", combined_result)

    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    main()