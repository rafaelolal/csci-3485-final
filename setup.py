from setuptools import find_packages, setup

# easy_embed/easy_embed
with open("easy_embed/README.md", "r") as f:
    long_description = f.read()

setup(
    name="easy_embed",  # easy_embed/src
    version="1.0.0",
    description="Simple self-hosted semantic search API",
    package_dir={"": "easy_embed"},  # easy_embed/easy_embed
    packages=find_packages(where="easy_embed"),  # easy_embed/easy_embed
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rafaelolal/csci-3485-final",
    author="Rafael Almeida",
    author_email="contact@ralmeida.dev",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "fastapi==0.115.6",
        "sentence-transformers==3.3.1",
        "sqlmodel==0.0.22",
    ],
    extras_require={
        "dev": ["pytest>=7.0", "twine>=4.0.2"],
    },
    python_requires="==3.12.8",
)
