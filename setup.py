# setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="beat-maker", # the name that you will install via pip
    version="1.3",
    author="Jason Robinson",
    author_email="robinsonjason761@gmail.com",
    description="An brief overview of the steps...",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/techthumb1/lambdata-techthumb1.git",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)