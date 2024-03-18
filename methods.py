import json

def verify_iam_role_policy(file_content: str) -> bool:
    if file_content is None:
        return False

    try:
        data = json.loads(file_content)
        if "PolicyDocument" in data and "Statement" in data["PolicyDocument"]:
            statements = data["PolicyDocument"]["Statement"]
            for statement in statements:
                if "Resource" in statement and statement["Resource"] == "*":
                    return False
            return True  # Return True if no statement with Resource: "*" found
        return False
    except (json.JSONDecodeError, KeyError):
        return False



    
# Unit tests
def test_verify_iam_role_policy():
    # Test case with valid policy (no asterisk in Resource field)
    valid_policy = '{"PolicyName": "root", "PolicyDocument": {"Version": "2012-10-17", "Statement": [{"Sid": "IamListAccess", "Effect": "Allow", "Action": ["iam:ListRoles", "iam:ListUsers"], "Resource": "arn:aws:iam::123456789012:role/*"}]}}'
    assert verify_iam_role_policy(valid_policy) == True

    # # Test case with invalid policy (asterisk in Resource field)
    invalid_policy = '{"PolicyName": "root", "PolicyDocument": {"Version": "2012-10-17", "Statement": [{"Sid": "IamListAccess", "Effect": "Allow", "Action": ["iam:ListRoles", "iam:ListUsers"], "Resource": "*"}]}}'
    assert verify_iam_role_policy(invalid_policy) == False

    # Test case with invalid JSON format
    invalid_json = '{"PolicyName": "root", "PolicyDocument": {"Version": "2012-10-17", "Statement": [{"Sid": "IamListAccess", "Effect": "Allow", "Action": ["iam:ListRoles", "iam:ListUsers"], "Resource": "*"'
    assert verify_iam_role_policy(invalid_json) == False

    # Test case with missing Resource field
    missing_resource_field = '{"PolicyName": "root", "PolicyDocument": {"Version": "2012-10-17", "Statement": [{"Sid": "IamListAccess", "Effect": "Allow", "Action": ["iam:ListRoles", "iam:ListUsers"]}]}}'
    assert verify_iam_role_policy(missing_resource_field) == True

    # Test case with empty input
    empty_input = ''
    assert verify_iam_role_policy(empty_input) == False

    # Test case with None input
    none_input = None
    assert verify_iam_role_policy(none_input) == False

    print("All tests passed successfully!")

# Run unit tests
test_verify_iam_role_policy()

with open("datas/data.json", 'r') as file:
    file_content = file.read()

print(verify_iam_role_policy(file_content))



