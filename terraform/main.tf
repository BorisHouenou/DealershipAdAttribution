resource "random_id" "suffix" {
  byte_length = 4
}

resource "aws_s3_bucket" "landing" {
  bucket = "${var.project_name}-landing-${random_id.suffix.hex}"
  acl    = "private"
  versioning { enabled = true }
}

data "aws_iam_policy_document" "lambda_assume" {
  statement {
    actions = ["sts:AssumeRole"]
    principals {
      type        = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }
  }
}

resource "aws_iam_role" "lambda_exec" {
  name               = "${var.project_name}-lambda-role"
  assume_role_policy = data.aws_iam_policy_document.lambda_assume.json
}

resource "aws_iam_role_policy_attachment" "lambda_logging" {
  role       = aws_iam_role.lambda_exec.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

resource "aws_redshiftserverless_namespace" "main" {
  namespace_name     = var.project_name
  admin_username     = "adminuser"
  admin_user_password = "ComplexPass123!"
}

resource "aws_redshiftserverless_workgroup" "wg" {
  workgroup_name      = "${var.project_name}-wg"
  namespace_name      = aws_redshiftserverless_namespace.main.namespace_name
  publicly_accessible = true
}
