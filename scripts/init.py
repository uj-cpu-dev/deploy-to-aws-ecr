import os

def write_nodejs_workflow():
    workflow = """
    name: Node.js Workflow
    on: push
    jobs:
      build:
        runs-on: ubuntu-latest
        steps:
          - name: Checkout
            uses: actions/checkout@v4
          - name: Setup Node.js
            uses: actions/setup-node@v3
            with:
              node-version: 16
          - name: Install dependencies
            run: npm install
    """
    with open(".github/workflows/nodejs.yml", "w") as f:
        f.write(workflow)

def write_java_workflow():
    workflow = """
    name: Java Workflow
    on: push
    jobs:
      build:
        runs-on: ubuntu-latest
        steps:
          - name: Checkout
            uses: actions/checkout@v4
          - name: Setup Java
            uses: actions/setup-java@v3
            with:
              java-version: 17
          - name: Build
            run: mvn clean verify
    """
    with open(".github/workflows/java.yml", "w") as f:
        f.write(workflow)

def main():
    if os.path.isfile("package.json"):
        write_nodejs_workflow()
    elif os.path.isfile("pom.xml"):
        write_java_workflow()
    else:
        print("Unknown project type. No workflow generated.")

if __name__ == "__main__":
    main()
