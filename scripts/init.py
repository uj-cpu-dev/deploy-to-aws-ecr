import os

def detect_language():
    if os.path.isfile("package.json"):
        return "nodejs"
    elif os.path.isfile("pom.xml"):
        return "java"
    else:
        return "unknown"

if __name__ == "__main__":
    language = detect_language()
    print(language)  # Outputs the language to standard output
