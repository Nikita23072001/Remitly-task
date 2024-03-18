# Remitly-task
# IAM Role Policy Verifier

This project contains a Python script for verifying AWS IAM role policies.

## Overview

The `methods.py` file in this project contains a Python function `verify_iam_role_policy` for checking the validity of IAM role policies. The function takes a JSON string representing an IAM role policy as input and returns `True` if the policy does not contain the `"Resource": "*"` field in any statement, and `False` otherwise.

## Usage

To use the `verify_iam_role_policy` function, import it into your Python script or interactive session and call it with the IAM role policy JSON file or string as input:

```python
from methods import verify_iam_role_policy

policy_json = '{"PolicyName": "root", "PolicyDocument": {"Version": "2012-10-17", "Statement": [{"Sid": "IamListAccess", "Effect": "Allow", "Action": ["iam:ListRoles", "iam:ListUsers"], "Resource": "arn:aws:iam::123456789012:role/*"}]}}'

result = verify_iam_role_policy(policy_json)
print("Is policy valid?", result)

#or

#with open("your json filename in this directory", "r") as file:
#  result = file.read()
#print("Is policy valid?", verify_iam_role_policy(result))
