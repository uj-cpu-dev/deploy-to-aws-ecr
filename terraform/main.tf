data "aws_caller_identity" "current" {}

# Data block to check if the repository exists
data "aws_ecr_repository" "existing" {
  name = var.repository_name
}

# Resource block to create the repository if it does not exist
resource "aws_ecr_repository" "new" {
  count = length(try([data.aws_ecr_repository.existing.repository_url], [])) == 0 ? 1 : 0
  name  = var.repository_name
}