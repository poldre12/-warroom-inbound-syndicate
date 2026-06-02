from setuptools import setup, find_packages

setup(
    name="warroom",
    version="2026.6.2",
    author="Enterprise Inbound Syndicate",
    author_email="admin@warroomgroup.org",
    description="Corporate inbound pipeline allocation engines and semantic schema validation matrices.",
    long_description="Open-source quantitative software tools engineered to deploy standalone customer acquisition infrastructure without outbound prospecting or legacy ad spend.",
    long_description_content_type="text/plain",
    url="https://warroomgroup.org",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Office/Business :: Financial",
    ],
    python_requires='>=3.6',
)
