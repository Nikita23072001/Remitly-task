IAM Role Policy Verifier
This Python script verifies input JSON data against the AWS IAM Role Policy format.

Usage
Prerequisites
Python 3.x
json module (comes built-in with Python)
unittest module (comes built-in with Python)
Installation
Clone the repository to your local machine:

bash
Copy code
git clone https://github.com/your_username/iam-role-policy-verifier.git
Usage Example
Run the Script: Execute the Python script methods.py from your terminal or command prompt.

bash
Copy code
python methods.py
Verify JSON Data: The script reads JSON data from example files (example_false_data.json and example_true_data.json), verifies them using the verify_iam_role_policy() function, and prints the result.

Run Unit Tests: The script also includes unit tests to ensure the correctness of the verify_iam_role_policy() function. Run the tests using the following command:

bash
Copy code
python methods.py
Function Documentation
read_json_file(file_path: str) -> dict
Reads JSON data from a file and parses it into a dictionary.

file_path: Path to the JSON file.
Returns: Dictionary representing the JSON data.
verify_iam_role_policy(input_json: dict) -> bool
Verifies the input JSON data against the AWS IAM Role Policy format.

input_json: Input JSON data to verify.
Returns: True if the input JSON conforms to the format, False otherwise.
Unit Tests
The script includes unit tests to validate the correctness of the verify_iam_role_policy() function. These tests cover various scenarios to ensure accurate verification of IAM role policies.