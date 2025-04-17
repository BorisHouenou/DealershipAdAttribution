output "landing_bucket" {
  description = "Name of the landing S3 bucket"
  value       = aws_s3_bucket.landing.id
}

output "lambda_role_arn" {
  value = aws_iam_role.lambda_exec.arn
}

output "redshift_endpoint" {
  value = aws_redshiftserverless_workgroup.wg.endpoint
}
