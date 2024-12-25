output "repository_exists" {
  value = length(data.aws_ecr_repository.existing) > 0 ? "exists" : "created"
}