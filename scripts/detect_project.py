import os
import sys

def detect_language(directory):
    # Implement your language detection logic here
    # For demonstration, we'll use placeholder values
    language = "Python"
    java_version = "11"
    node_version = "14"

    # Set outputs
    with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
        print(f'language={language}', file=fh)
        print(f'java_version={java_version}', file=fh)
        print(f'node_version={node_version}', file=fh)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python detect_project.py <directory>")
        sys.exit(1)
    directory = sys.argv[1]
    detect_language(directory)
