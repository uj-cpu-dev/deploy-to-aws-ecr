import subprocess
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def setup_java():
    logger.info("Setting up Java environment")
    subprocess.run(['sudo', 'apt-get', 'update'], check=True)
    subprocess.run(['sudo', 'apt-get', 'install', '-y', 'maven'], check=True)

def setup_nodejs():
    logger.info("Setting up Node.js environment")
    subprocess.run(['curl', '-sL', 'https://deb.nodesource.com/setup_14.x'], check=True)
    subprocess.run(['sudo', 'bash', '-'], check=True)
    subprocess.run(['sudo', 'apt-get', 'install', '-y', 'nodejs'], check=True)

def setup_python():
    logger.info("Setting up Python environment")
    subprocess.run(['sudo', 'apt-get', 'update'], check=True)
    subprocess.run(['sudo', 'apt-get', 'install', '-y', 'python3-pip'], check=True)

def setup_environment(detected_language):
    setup_actions = {
        'java': setup_java,
        'nodejs': setup_nodejs,
        'python': setup_python,
    }
    setup_action = setup_actions.get(detected_language)
    if setup_action:
        setup_action()
    else:
        logger.warning(f"Language '{detected_language}' not supported or setup not required")

if __name__ == "__main__":
    import sys
    detected_language = sys.argv[1]  # Access the first argument (language)
    setup_environment(detected_language)