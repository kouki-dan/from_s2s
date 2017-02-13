
from setuptools import setup, find_packages

setup(
    name="from s2s",
    version="0.1",
    packages=find_packages(),
    test_suite="test",
    install_requires=[
        "slackbot",
        "requests",
    ],
)

