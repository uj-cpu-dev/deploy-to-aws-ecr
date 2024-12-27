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

def detect_language():
    logger.info("Detecting project language...")
    if os.path.exists("package.json"):
        logger.info("Detected Node.js project (package.json found).")
        return "nodejs"
    elif os.path.exists("pom.xml"):
        logger.info("Detected Java project (pom.xml found).")
        return "java"
    elif os.path.exists("build.gradle"):
        logger.info("Detected Gradle project (build.gradle found).")
        return "gradle"
    elif os.path.exists("go.mod"):
        logger.info("Detected Go project (go.mod found).")
        return "go"
    elif os.path.exists("Gemfile"):  # Example for Ruby
        logger.info("Detected Ruby project (Gemfile found).")
        return "ruby"
    elif os.path.exists("pyproject.toml") or os.path.exists("setup.py"):  # Example for Python
        logger.info("Detected Python project (pyproject.toml or setup.py found).")
        return "python"
    else:
        logger.warning("No recognizable project files found. Language detection returned 'unknown'.")
        return "unknown"

if __name__ == "__main__":
    logger.debug("Script execution started.")
    language = detect_language()
    print(f"::set-output name=language::{language}")

    if language == "nodejs":
        try:
            with open("package.json", "r") as f:
                package_json = json.load(f)
                node_version = package_json.get("engines", {}).get("node", "16")
                logger.info(f"Node.js version found: {node_version}")
                print(f"::set-output name=node_version::{node_version}")
        except FileNotFoundError:
            logger.warning("package.json file not found.")
            print("::warning file=package.json::package.json not found")
        except json.JSONDecodeError as e:
            logger.warning(f"Invalid JSON in package.json: {e}")
            print(f"::warning file=package.json::Invalid JSON in package.json: {e}")
    elif language == "java":
        try:
            tree = ET.parse('pom.xml')
            root = tree.getroot()
            ns = {'mvn': 'http://maven.apache.org/POM/4.0.0'}
            java_version_element = root.find('.//mvn:properties/mvn:java.version', namespaces=ns)
            if java_version_element is not None:
                java_version = java_version_element.text
                logger.info(f"Java version found: {java_version}")
                print(f"::set-output name=java_version::{java_version}")
            else:
                logger.warning("java.version not found in pom.xml")
                print("::warning file=pom.xml::java.version not found in pom.xml")
        except FileNotFoundError:
            logger.warning("pom.xml file not found.")
            print("::warning file=pom.xml::pom.xml not found")
        except ET.ParseError as e:
            logger.warning(f"Invalid XML in pom.xml: {e}")
            print(f"::warning file=pom.xml::Invalid XML in pom.xml: {e}")

    logger.debug("Script execution finished.")
