from setuptools import setup, find_packages
import os

# Read the README.md file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, "./../README.md"), encoding="utf-8") as f:
    long_description = f.read()

# Read requirements.txt for dependencies
with open(os.path.join(this_directory, "requirements.txt"), encoding="utf-8") as f:
    requirements = f.read().splitlines()

setup(
    name="BreezeUI",
    version="0.0.0",
    author="AK",
    author_email="ak@stellar-code.com",
    url="https://github.com/TRC-Loop/BreezeUI",
    description="BreezeUI is a Python GUI Library, which focuses on simplicity and customizability.",
    long_description=long_description,  # Set the long description
    long_description_content_type="text/markdown",  # Specify the content type
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=requirements,  # Set dependencies from requirements.txt
    python_requires=">=3.9",
)
