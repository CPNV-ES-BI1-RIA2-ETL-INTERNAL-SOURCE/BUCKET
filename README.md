# Bucket

## Description

The aim is to offer a service for connecting and using a bucket of different services such as S3 or GCP.

---

## Getting Started

### Prerequisites

List all dependencies and their version needed by the project as :
* Python 3.13 or later [official doc](https://www.python.org/downloads/)
* Git version 2.47.1 or later [official doc](https://git-scm.com/)
* Docker desktop version 4.36.0 or later [official doc](https://www.docker.com/products/docker-desktop/)

Here are few more dependencies need for Development : 
* IDE used pycharm 2024.3 or later [official doc](https://www.jetbrains.com/pycharm/download/?section=windows)
* Pipenv version 2024.4.0 or later [official doc](https://pipenv.pypa.io/en/latest/)

---

### Configuration

#### Production environment

Copy and modify the .env file.
````shell
cp .env.example .env
````

Build the docker container.
````shell
docker build -t bucket_conector . 
````

Run the docker container.
````shell
docker run -d -p 8000:8000 bucket_conector
````

Check container.
````shell
docker container ls -a
````

The server is running on : [http://localhost:8000](http://localhost:8000)

To have the information about the api go to : [http://localhost:8000/docs](http://localhost:8000/docs)

---

#### Development environment

If not already done, install pipenv with python. 
````shell
pip install pipenv
````

Then check the version : 
````shell
pipenv --version
````

Enter the virtual environment : 
````shell
pipenv shell
````

Install all dependencies : 
````shell
pipenv install --dev
````

Copy and modify the .env file.
````shell
cp .env.example .env
````

Then run the server locally.
````shell
fastapi.exe run --port 8000
````

The server is running on : [http://localhost:8000](http://localhost:8000)

To have the information about the api go to : [http://localhost:8000/docs](http://localhost:8000/docs)

## Testing

To run all tests : 
````shell
pytest
````

To run a specific test :
````shell
pytest tests/aws/test_load.py
````

## Directory structure

````shell
├───app                   # Source code (application content) 
│   ├───cloud_provider
│   ├───exceptions
│   ├───routes            
│   ├───schemas           # Schema to define input and output of the api
│   │   ├───requests
│   │   ├───responses
│   ├───services
│   ├───main.py           # Entrypoint
├───docs                  # Documentation
├───tests                 # Tests 
├───.env.example     
├───Dockerfile            # Docker image configuration 
├───Pipfile               # Dependencies
└───Pipfile.lock           
````

## Collaborate

* Workflow
    * [Gitflow](https://www.atlassian.com/fr/git/tutorials/comparing-workflows/gitflow-workflow#:~:text=Gitflow%20est%20l'un%20des,les%20hotfix%20vers%20la%20production.)
    * [How to commit](https://www.conventionalcommits.org/en/v1.0.0/)
    * [How to use your workflow](https://nvie.com/posts/a-successful-git-branching-model/)

    * Propose a new feature in [Github issues](https://github.com/CPNV-ES-BI1-SBB/EXTERNAL-SOURCE-LOAD-DATALAKE/issues)
    * Pull requests are open to merge in the develop branch.
    * Release on the main branch we use GitFlow and not with GitHub release.
    * Issues are added to the [github issues page](https://github.com/CPNV-ES-BI1-SBB/EXTERNAL-SOURCE-LOAD-DATALAKE/issues)

### Commits
* [How to commit](https://www.conventionalcommits.org/en/v1.0.0/)
```shell
<type>(<scope>): <subject>
```

- **build**: Changes that affect the build system or external dependencies (e.g., npm, make, etc.).
- **ci**: Changes related to integration or configuration files and scripts (e.g., Travis, Ansible, BrowserStack, etc.).
- **feat**: Adding a new feature.
- **fix**: Bug fixes.
- **perf**: Performance improvements.
- **refactor**: Modifications that neither add a new feature nor improve performance.
- **style**: Changes that do not affect functionality or semantics (e.g., indentation, formatting, adding spaces, renaming a variable, etc.).
- **docs**: Writing or updating documentation.
- **test**: Adding or modifying tests.

examples :
```shell
feat(MyClass): add a button in the ...
````
```shell
feat(example.js): change name into username
````

---

## License
The project is released under a [MIT license](https://mit-license.org/)

---

## Contact
* If needed you can create an issue on GitHub we will try to respond as quickly as possible.
