import subprocess
import logging
import os
import sys
import xml.etree.ElementTree as ET

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def run_tests(language, repo_path):
    os.chdir(repo_path)
    try:
        if language == 'java':
            logger.info("Running Java tests using Maven...")
            # Determine Java version from pom.xml (replace with your preferred method)
            java_version = 17

            # Set up Java dynamically
            if java_version:
                setup_java(java_version) 
            else:
                logger.warning("Could not determine Java version from pom.xml. Using default.")
                # Use a default Java version if not found
                setup_java("11")  # Example: Default to Java 11

            subprocess.run(['mvn', 'clean', 'verify'], check=True) 
        elif language == 'nodejs':
            logger.info("Running Node.js tests using npm...")
            subprocess.run(['npm', 'install'], check=True)
            subprocess.run(['npm', 'test'], check=True)
        elif language == 'python':
            logger.info("Running Python tests using pytest...")
            subprocess.run(['pip', 'install', '-r', 'requirements.txt'], check=True)
            subprocess.run(['pytest'], check=True)
        else:
            logger.warning(f"Test execution for '{language}' is not supported.")
    except subprocess.CalledProcessError as e:
        logger.error(f"Test execution failed: {e}")
        sys.exit(1)
    except Exception as e:
        logger.error(f"An error occurred during test execution: {e}")
        sys.exit(1)

def get_java_version_from_pom():
    """
    Extracts the Java version from the pom.xml file.

    Returns:
        str: The Java version extracted from the pom.xml file.
    """
    try:
        tree = ET.parse('pom.xml')  # Parse the pom.xml file
        root = tree.getroot()
        java_version = root.find('.//properties/java.version').text
        return java_version
    except FileNotFoundError:
        print("Error: pom.xml not found.")
        return None
    except Exception as e:
        print(f"Error extracting Java version from pom.xml: {e}")
        return None

def setup_java(java_version):
    """
    Sets up the Java environment using the specified version.
    """
    try:
        subprocess.run(["java", "-version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    except subprocess.CalledProcessError:
        # Install Java if not already installed
        subprocess.run(["sudo", "apt-get", "update"], check=True)
        subprocess.run(["sudo", "apt-get", "install", f"openjdk-{java_version}-jdk"], check=True)


if __name__ == "__main__":
    repo_path = os.path.abspath("global-repository")
    detected_language = sys.argv[1]
    if detected_language is None:
        logger.error("Could not detect project language.")
        sys.exit(1)
    run_tests(detected_language, repo_path)