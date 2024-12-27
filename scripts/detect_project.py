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
    if os.path.exists(os.path.join(base_path, "package.json")):
        logger.info("Detected Node.js project (package.json found).")
        return "nodejs"
    elif os.path.exists(os.path.join(base_path, "pom.xml")):
        logger.info("Detected Java project (pom.xml found).")
        return "java"
    elif os.path.exists(os.path.join(base_path, "build.gradle")):
        logger.info("Detected Gradle project (build.gradle found).")
        return "gradle"
    elif os.path.exists(os.path.join(base_path, "go.mod")):
        logger.info("Detected Go project (go.mod found).")
        return "go"
    elif os.path.exists(os.path.join(base_path, "Gemfile")):  # Example for Ruby
        logger.info("Detected Ruby project (Gemfile found).")
        return "ruby"
    elif os.path.exists(os.path.join(base_path, "pyproject.toml")) or os.path.exists(os.path.join(base_path, "setup.py")):  # Example for Python
        logger.info("Detected Python project (pyproject.toml or setup.py found).")
        return "python"
    else:
        logger.warning("No recognizable project files found. Language detection returned 'unknown'.")
        return "unknown"

if __name__ == "__main__":
    repo_path = os.path.abspath("global-repository")
    logger.debug(f"Scanning repository at: {repo_path}")
    language = detect_language(repo_path)
    print(f"::set-output name=language::{language}")
