import os
import json
import logging
import xml.etree.ElementTree as ET

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.WARNING)  # Set warning level

def detect_language():
    if os.path.exists("package.json"):
        return "nodejs"
    elif os.path.exists("pom.xml"):
        return "java"
    elif os.path.exists("build.gradle"):
        return "gradle"
    elif os.path.exists("go.mod"):
        return "go"
    elif os.path.exists("Gemfile"):  # Example for Ruby
        return "ruby"
    elif os.path.exists("pyproject.toml") or os.path.exists("setup.py"): # Example for python
        return "python"
    else:
        return "unknown"

if __name__ == "__main__":
    language = detect_language()
    print(f"::set-output name=language::{language}")

    if language == "nodejs":
        try:
            with open("package.json", "r") as f:
                package_json = json.load(f)
                node_version = package_json.get("engines", {}).get("node", "16")
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