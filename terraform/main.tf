data "aws_caller_identity" "current" {}

# Check if the repository exists
data "aws_ecr_repository" "existing" {
  name = var.repository_name
  # Suppress errors if the repository does not exist
  lifecycle {
    ignore_errors = true
  }
}

# Create a new repository only if it does not exist
resource "aws_ecr_repository" "repository" {
  count = data.aws_ecr_repository.existing.id == "" ? 1 : 0

  name                 = var.repository_name
  image_tag_mutability = "IMMUTABLE"
  image_scanning_configuration {
    scan_on_push = true
  }
}