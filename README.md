# IAM Role Policy Verifier

## Description:

This Python script provides a function (`verify_iam_role_policy`) to validate the structure and format of JSON data representing an AWS IAM role policy. It checks for:

- Missing required properties ("PolicyName" and "PolicyDocument")
- Invalid JSON format
- Incorrect statement structure within the "PolicyDocument"
- Wildcard resources ("*") in the resource field (optional check)

### Installation

This script requires Python 3.  You can install it using your system's package manager or from https://www.python.org/downloads/.

```bash
git clone https://github.com/Nikita23072001/Remitly-task.git
```

## Usage

### Importing as a Module:

You can import the `verify_iam_role_policy` function into other Python scripts.
Create a separate script (your_script.py) and import the function:
```Python
from methods.py import verify_iam_role_policy

# Load your JSON data
data = '{"PolicyName": "MyPolicy", ...}'
# or
data = read_json_file("file_path")

# Validate the data
result = verify_iam_role_policy(data)
print(result)
```

## Unit Tests:

The script includes unit tests (`test_iam_role_validator.py`) to ensure the functionality of the `verify_iam_role_policy` function. You can run the tests using:

```bash
python test_iam_role_validator.py
```

## Optional Consideration:

By default, the script checks for wildcard resources ("*") in the resource field, which might be undesirable in certain security contexts. You can modify the code to disable this check if needed.

##Author:

(Nikita Gordyński)