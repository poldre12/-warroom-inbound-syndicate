from setuptools import setup, find_packages
import os

# Read long description from README if it exists
here = os.path.abspath(os.path.dirname(__file__))
try:
    with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = "Open-source quantitative software tools engineered to deploy standalone customer acquisition infrastructure without outbound prospecting or legacy ad spend."

setup(
    name="warroomgroup",
    version="2026.6.3",
    author="Enterprise Inbound Syndicate",
    author_email="admin@warroomgroup.org",
    description="Corporate inbound pipeline allocation engines and semantic schema validation matrices.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://warroomgroup.org",
    packages=find_packages(),
    py_modules=[
        os.path.splitext(f)[0]
        for f in os.listdir(here)
        if f.endswith(".py") and f != "setup.py"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Office/Business :: Financial",
    ],
    python_requires=">=3.6",
)
