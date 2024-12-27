import os
from guesslang import Guess

def read_file_content(file_path):
    try:
        with open(file_path, 'r', errors='ignore') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return ""

def detect_dominant_language(repo_path):
    guess = Guess()
    language_count = {}

    for root, _, files in os.walk(repo_path):
        for file in files:
            file_path = os.path.join(root, file)
            content = read_file_content(file_path)
            if content:
                language = guess.language_name(content)
                if language:
                    language_count[language] = language_count.get(language, 0) + 1

    if language_count:
        dominant_language = max(language_count, key=language_count.get)
        return dominant_language
    else:
        return "Unknown"

if __name__ == "__main__":
    repo_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dominant_language = detect_dominant_language(repo_path)
    print(f"Dominant programming language: {dominant_language}")
