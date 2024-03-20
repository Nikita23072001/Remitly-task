import json
import boto3
import unittest

def read_json_file(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        json_data = json.load(file)
    return json_data

def verify_iam_role_policy(input_json: dict) -> bool:

    """
    Verify the input JSON data against the AWS::IAM::Role Policy format.

    Parameters:
        input_json (dict): The input JSON data to verify.

    Returns:
        bool: True if the input JSON conforms to the format, False otherwise.
    """

    # Ensure input_json is a dictionary
    if not isinstance(input_json, dict):
        return False
    
    # Ensure 'Version' and 'Statement' keys are present
    if 'Version' not in input_json or 'Statement' not in input_json:
        return False
    
    # Ensure 'Statement' is a list
    if not isinstance(input_json['Statement'], list):
        return False
    
    # Ensure each statement in 'Statement' is a dictionary with required keys
    for statement in input_json['Statement']:
        if not isinstance(statement, dict):
            return False
        if 'Effect' not in statement or 'Action' not in statement or 'Resource' not in statement:
            return False
        if 'Resource' not in statement or statement['Resource'] == '*':
            return False

    # If all checks passed, return True
    return True

file1 = read_json_file('example_false_data.json')
file2 = read_json_file('example_true_data.json')
print(verify_iam_role_policy(file1))
print(verify_iam_role_policy(file2))

class TestVerifyIAMRolePolicy(unittest.TestCase):
    def test_valid_policy(self):
        input_json = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Action": "s3:GetObject",
                    "Resource": "arn:aws:s3:::example-bucket/*"
                }
            ]
        }
        self.assertTrue(verify_iam_role_policy(input_json))

    def test_missing_version_key(self):
        input_json = {
            "Statement": [
                {
                    "Effect": "Allow",
                    "Action": "s3:GetObject",
                    "Resource": "arn:aws:s3:::example-bucket/*"
                }
            ]
        }
        self.assertFalse(verify_iam_role_policy(input_json))

    def test_missing_statement_key(self):
        input_json = {
            "Version": "2012-10-17"
        }
        self.assertFalse(verify_iam_role_policy(input_json))

    def test_statement_not_list(self):
        input_json = {
            "Version": "2012-10-17",
            "Statement": {}
        }
        self.assertFalse(verify_iam_role_policy(input_json))

    def test_invalid_statement_structure(self):
        input_json = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Resource": "arn:aws:s3:::example-bucket/*"
                }
            ]
        }
        self.assertFalse(verify_iam_role_policy(input_json))

    def test_invalid_resource(self):
        input_json = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Action": "s3:GetObject",
                    "Resource": "*"
                }
            ]
        }
        self.assertFalse(verify_iam_role_policy(input_json))

if __name__ == '__main__':
    unittest.main()