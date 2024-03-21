import unittest
from methods import verify_iam_role_policy

class TestVerifyIAMRolePolicy(unittest.TestCase):

  def test_valid_iam_role_policy(self):
    data = """
    {
      "PolicyName": "MyPolicy",
      "PolicyDocument": {
        "Statement": [
          {
            "Effect": "Allow",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::my-bucket"
          }
        ]
      }
    }
    """
    self.assertTrue(verify_iam_role_policy(data))

  def test_invalid_json(self):
    data = "This is not JSON"
    self.assertFalse(verify_iam_role_policy(data))

  def test_missing_properties(self):
    data = """
    {
      "PolicyDocument": {
        "Statement": []
      }
    }
    """
    self.assertFalse(verify_iam_role_policy(data))

  def test_invalid_statement_structure(self):
    data = """
    {
      "PolicyDocument": {
        "Statement": [
          "Invalid statement"
        ]
      }
    }
    """
    self.assertFalse(verify_iam_role_policy(data))
  def test_wildcard_resource(self):
    data = """
    {
      "PolicyName": "MyPolicy",
      "PolicyDocument": {
        "Statement": [
          {
            "Effect": "Allow",
            "Action": "s3:GetObject",
            "Resource": "*"
          }
        ]
      }
    }
    """
    self.assertFalse(verify_iam_role_policy(data))


if __name__ == "__main__":
  unittest.main()