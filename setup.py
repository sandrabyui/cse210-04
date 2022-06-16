""" Setup file for pip install -e support
"""
from setuptools import setup

with open("README.md", "r") as in_file:
    markdown = in_file.read()

with open("requirements.txt", "r") as in_file:
    reqs = [line.strip() for line in in_file.readlines()]

setup(
    name="didt",
    author="BYUI Student",
    author_email="example@example.com",
    url="https://github.com/Eugenespace/cse210-08",
    license="MIT",
    license_files=["LICENSE.md"],
    description="Tool for checking if all modules, classes, and functions have docstrings",
    version="0.1.0",
    long_description=markdown,
    packages=["cyclegame"],
    entry_points={"console_scripts": [
        "cyclegame=cyclegame.__main__:main"]},
    install_requires=reqs,
)
