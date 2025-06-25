# This is a setup.py file for a Python package.
# It uses setuptools to package the source code located in the "src" directory.
#  it will look for constructor.py files in the "src" directory and its subdirectories to identify the packages and install this package as my local package.
# to intsall this package as a local package, we need setup.py file. 


import setuptools


with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "End-to-End-MLflow-Project"
AUTHOR_USER_NAME = "Dinesh0394"
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "dineshbabu0394@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for ml app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)