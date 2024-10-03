Project Setup istruction
=============

1. Installed Python 3.12:
    * Installed Python 3.12 using Homebrew.
2. Configured pyenv (Optional):
    * Installed pyenv and used it to manage Python versions.
    * Set Python 3.12 as the local version for your project directory.
3. Created a New Project Directory:
    * Created and navigated to a new directory for your project.
4. Installed Poetry:
    * Installed Poetry using the installation script.
5. Configured Poetry to Use Python 3.12:
    * Configured Poetry to use Python 3.12 for the new project.
6. Initialized a New Poetry Project:
    * Created a new Poetry project in the directory.
7. Updated pyproject.toml:
    * Updated pyproject.toml to specify Python 3.12.
8. Installed Dependencies and Activated Poetry Shell:
    * Installed any necessary dependencies using Poetry.
    * Activated the Poetry virtual environment

Clean the pyproject.toml and poetry.lock Files
* If you want to start fresh with the pyproject.toml and poetry.lock files, you can delete them and recreate the project:
Delete the poetry.lock File:
* rm poetry.lock => copy and run this to remove insatlled packages
other way of removing the packages installed is
* pip unistall -r requirements.txt -y
*
Basic python package to update or install
python -m pip install --upgrade pip
python -m pip install --upgrade setuptools
python -m pip install wheel
find this
command = >
pip list
Package    Version
---------- -------
pip        24.2
setuptools 74.1.2
wheel      0.44.0
python virtualenv
python -m venv venv
source venv/bin/activate

Third party virtualenv
	python -m pip install virtualenv
poetry install
	1.	curl -sSL https://install.python-poetry.org | python3 - => 	this 	is now depricated (check the poetry official site 	poetry.org)
	2.	pip install poetry
	3. 	pipx install poetry. (new package manager in python family)

poetry packaging
	1.	poetry init
	2.	give meta descriptions for package/proejct
	3. 	leave blank and enter for not adding package and start fresh

now add packages in the dependecies section of pyproject.toml and run
	1. poetry install --no-root or poetry install

Automate Sorting with Pre-Commit Hook
To ensure that the pyproject.toml file remains consistently formatted, set up a pre-commit hook using toml-sort. This process will automatically sort the file every time you make a commit.
Steps:
Install pre-commit: Add pre-commit as a development dependency in your project.command => poetry add --group dev pre-commit
Create .pre-commit-config.yaml: In your project root, create a .pre-commit-config.yaml file with the following content:============repos:
  - repo: https://github.com/pappasam/toml-sort
    rev: "v0.23.1"  # Use the latest stable version
    hooks:
      - id: toml-sort
=============

Install the Pre-Commit Hook: Run the following command to install the pre-commit hook.
======pre-commit install
======
Now, every time you commit changes, toml-sort will automatically format the pyproject.toml file.



List of files to be installed for proejct aptment
#graphene-django = "^3.0.0"  # For GraphQL
#django-filter = "^23.1"  # Filtering support for DRF
#asgiref = "^3.7.2"  # Async server and interface
#gunicorn = "^22.0.0"  # Production WSGI Server
#redis = "^5.0.1"  # For caching and background task queues
#celery = "^5.3"  # Task queue (used for handling asynchronous tasks)

# Database
#psycopg = { version = "^3.1.8", extras = ["binary"] }  # PostgreSQL connector

# Testing & Linting
#pytest = "^8.0.0"
#pytest-django = "^4.8.0"
#pytest-cov = "^5.0.0"  # Coverage report
#ruff = "^0.5.4"  # Linting
#coverage = "^7.2"  # Code coverage

# Static and Media Handling
pillow = "^10.3.0"  # Image handling

# For GraphQL
#graphql-core = "^3.2.0"
#promise = "^2.3"  # For handling async in GraphQL

# Utilities
#python-dateutil = "^2.8.2"
#pytz = "^2024.1"

[tool.poetry.group.dev.dependencies]
#django-debug-toolbar = "^4.0"
#django-extensions = "^3.1.2"  # For extensions such as shell_plus
#pytest-asyncio = "^0.23.7"
#freezegun = "^1.0.0"  # For testing with time-sensitive code
#pre-commit = "^3.4"  # Linting and code checks before commits


installed and specified in pip and poetry lock.
===
[tool.poetry]
name = "practice-appointment"
version = "1.0.1"
description = "This is an appoinment system built using Python, Django for GraphQL API and NextJs. It is highly moduler and headless."
authors = ["Suman Sunuwar <jaycessunuwar@gmail.com>"]
license = "MIT"
readme = "README.md"

[tool.poetry.dependencies]
python = "~3.12"
django = { version = "^4.2", extras = ["bcrypt"] }
graphene = "^3.3"
psycopg = "^3.2.1"
django-filter = "^24.3"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"


In the pip freeze list > requirements.txt
aniso8601==9.0.1
asgiref==3.8.1
bcrypt==4.2.0
build==1.2.2
CacheControl==0.14.0
certifi==2024.8.30
cffi==1.17.1
charset-normalizer==3.3.2
cleo==2.1.0
crashtest==0.4.1
distlib==0.3.8
Django==4.2.16
django-filter==24.3
dulwich==0.21.7
fastjsonschema==2.20.0
filelock==3.16.0
graphene==3.3
graphql-core==3.2.4
graphql-relay==3.2.0
idna==3.8
installer==0.7.0
jaraco.classes==3.4.0
keyring==24.3.1
more-itertools==10.5.0
msgpack==1.1.0
packaging==24.1
pexpect==4.9.0
pkginfo==1.11.1
platformdirs==4.3.2
poetry==1.8.3
poetry-core==1.9.0
poetry-plugin-export==1.8.0
psycopg==3.2.1
ptyprocess==0.7.0
pycparser==2.22
pyproject_hooks==1.1.0
rapidfuzz==3.9.7
requests==2.32.3
requests-toolbelt==1.0.0
setuptools==74.1.2
shellingham==1.5.4
sqlparse==0.5.1
tomlkit==0.13.2
trove-classifiers==2024.7.2
typing_extensions==4.12.2
urllib3==2.2.2
virtualenv==20.26.4
wheel==0.44.0
xattr==1.1.0


Initial project setup / configuration with django settings convention

commands

mkdir local
cp ./config/settings/templates/settings.dev.py ./local/settings.dev.py
#this is where the local settings (non prod) are overridden by the developers
