import subprocess
import sys
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def run_tests(language, repo_path):
    os.chdir(repo_path)
    try:
        if language == 'java':
            logger.info("Running Java tests using Maven...")
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

if __name__ == "__main__":
    repo_path = os.path.abspath("global-repository")
    if len(sys.argv) != 2:
        logger.error("Usage: python run_tests.py <language>")
        sys.exit(1)
    detected_language = sys.argv[1]
    run_tests(detected_language, repo_path)
