data "aws_caller_identity" "current" {}

data "aws_ecr_repository" "existing" {
  name = var.repository_name
}

resource "null_resource" "create_repository" {
  triggers {
    # Check if the repository exists (data can be empty)
    provider = data.aws_ecr_repository.existing.empty == false ? aws.ecr : null
  }

  provisioner "local-exec" {
    command = "aws ecr create-repository --repository-name ${var.repository_name}"
    # Only run if the data is empty (i.e., repository doesn't exist)
    when = data.aws_ecr_repository.existing.empty
  }
}