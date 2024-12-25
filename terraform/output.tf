output "repository_exists" {
  value = length(try([data.aws_ecr_repository.existing.repository_url], [])) > 0 ? "exists" : "created"
}