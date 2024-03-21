import json

def read_json_file(file_path: str) -> str:
    """
    This function reads the content of a JSON file from the given path and returns it as a string.
    """
    with open(file_path, 'r') as file:
        file_content = file.read()
        return file_content

def verify_iam_role_policy(data: str) -> bool:
  """
  This function checks if the input data is a valid JSON representation of an AWS::IAM::Role Policy,
  including checks for missing properties and wildcard resources.

  Args:
      data: The input data to be checked.

  Returns:
      True if the data is a valid IAM role policy, False otherwise.
  """
  try:
    # Try to parse the data as JSON
    parsed_data = json.loads(data)
  except json.JSONDecodeError:
    return False

  # Check for required properties
  required_props = {"PolicyDocument", "PolicyName"}  # Include both properties
  missing_props = required_props - set(parsed_data.keys())
  if missing_props:
    return False

  # Validate PolicyDocument structure (considering different actions)
  if not isinstance(parsed_data["PolicyDocument"], dict) or "Statement" not in parsed_data["PolicyDocument"]:
    return False
  for statement in parsed_data["PolicyDocument"]["Statement"]:
    if not isinstance(statement, dict) or not all(key in statement for key in ("Effect", "Action", "Resource")):
      return False
    # Wildcard resource check
    if statement["Resource"] == "*":
        print(statement["Resource"])
        return False

  return True

#My check if works as expected
# file1 = read_json_file('example_false_data.json')
print(verify_iam_role_policy(read_json_file('example_false_data.json')))
print(verify_iam_role_policy(read_json_file('example_true_data.json')))