variable "bucket" {
  type = string
  default= ""
}

variable "role_arn" {
  type = string
  default= ""
}

variable "region" {
  type = string
  default= ""
}

variable "key" {
  type = string
  default= ""
}

variable "dynamodb_table" {
  type = string
  default= ""
}

variable "repository_name" {
  description = "Name of the ECR repository"
  type        = string
  validation {
    condition     = length(var.repository_name) >= 2 && length(var.repository_name) <= 256
    error_message = "Repository name must be between 2 and 256 characters long."
  }
}
