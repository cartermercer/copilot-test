provider "aws" {
  region = "us-east-1" # Replace with your desired AWS region
}

resource "aws_iam_role" "lambda_role" {
  name = "lambda_execution_role"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}

resource "aws_lambda_function" "pipeline_function" {
  function_name = "pipeline_function"
  role          = aws_iam_role.lambda_role.arn
  handler       = "pipeline.main"
  runtime       = "python3.9"

  filename         = "pipeline.zip"
  source_code_hash = filebase64sha256("pipeline.zip")
}

resource "null_resource" "package_lambda" {
  provisioner "local-exec" {
    command = "zip pipeline.zip ../pipeline.py"
  }

  triggers = {
    always_run = timestamp()
  }
}