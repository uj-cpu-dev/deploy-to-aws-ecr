import os
import json
import logging
import xml.etree.ElementTree as ET

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,  # Set to DEBUG to capture all log messages
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def detect_language(base_path):
    logger.info("Detecting project language...")

    # Define file-to-language mappings
    project_files = {
        "nodejs": "package.json",
        "java": "pom.xml",
        "gradle": "build.gradle",
        "go": "go.mod",
        "ruby": "Gemfile",
        "python": ["pyproject.toml", "setup.py"],
        "docker": "Dockerfile",
        "make": "Makefile",
        "typescript": "tsconfig.json",
        "php": "composer.json",
        "rust": "Cargo.toml",
    }

    # Check for the presence of files
    for language, files in project_files.items():
        if isinstance(files, list):
            for file in files:
                if os.path.exists(os.path.join(base_path, file)):
                    logger.info(f"Detected {language} project ({file} found).")
                    return language
        else:
            if os.path.exists(os.path.join(base_path, files)):
                logger.info(f"Detected {language} project ({files} found).")
                return language

    logger.warning("No recognizable project files found. Language detection returned 'unknown'.")
    return "unknown"

def main():
    repo_path = os.path.abspath("global-repository")
    logger.debug(f"Scanning repository at: {repo_path}")

    try:
        language = detect_language(repo_path)
        print(f"::set-output name=language::{language}")
    except Exception as e:
        logger.error(f"Error during language detection: {e}")
        print(f"::error::Error during language detection: {e}")

if __name__ == "__main__":
    main()
