# Rule-Engine-with-AST
Running the Script
   - Make sure you are in the correct directory in your terminal/command prompt where the `rule_engine.py` file is located.

Step-by-Step Troubleshooting

Run the Script
   - Open your terminal (or command prompt) and navigate to the folder where you saved `rule_engine.py` using the `cd` command. For example:
     ```bash
     cd path/to/your/folder
     ```
Execute the Script
   - Run the script using Python:
     ```bash
     python rule_engine.py
     ```
   - If you have multiple versions of Python installed, you may need to use `python3` instead:
     ```bash
     python3 rule_engine.py
     ```

Check the Error Message
   - If you receive an error message, take note of what it says. Common messages might indicate:
     - **NameError**: A variable or function was referenced before assignment.
     - **ValueError**: There's an issue with unpacking or data types.
     - **ImportError**: A required module is not found.

Debugging Output
   - If you encounter errors, modify the `main` function to include print statements before key operations to help pinpoint where things go wrong. For example:
     ```python
     def main():
         print("Starting rule creation...")
