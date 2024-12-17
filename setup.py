from setuptools import find_packages, setup

# easy_embed/easy_embed
with open("easy_embed/README.md", "r") as f:
    long_description = f.read()

setup(
    name="easy-embed-rafaelolal",  # easy_embed/src
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
        "annotated-types==0.7.0",
        "anyio==4.7.0",
        "certifi==2024.12.14",
        "charset-normalizer==3.4.0",
        "click==8.1.7",
        "dnspython==2.7.0",
        "email_validator==2.2.0",
        "fastapi==0.115.6",
        "fastapi-cli==0.0.7",
        "filelock==3.16.1",
        "fsspec==2024.10.0",
        "h11==0.14.0",
        "httpcore==1.0.7",
        "httptools==0.6.4",
        "httpx==0.28.1",
        "huggingface-hub==0.26.5",
        "idna==3.10",
        "Jinja2==3.1.4",
        "joblib==1.4.2",
        "markdown-it-py==3.0.0",
        "MarkupSafe==3.0.2",
        "mdurl==0.1.2",
        "mpmath==1.3.0",
        "networkx==3.4.2",
        "numpy==2.2.0",
        "packaging==24.2",
        "pillow==11.0.0",
        "pydantic==2.10.3",
        "pydantic_core==2.27.1",
        "Pygments==2.18.0",
        "python-dotenv==1.0.1",
        "python-multipart==0.0.19",
        "PyYAML==6.0.2",
        "regex==2024.11.6",
        "requests==2.32.3",
        "rich==13.9.4",
        "rich-toolkit==0.12.0",
        "safetensors==0.4.5",
        "scikit-learn==1.6.0",
        "scipy==1.14.1",
        "sentence-transformers==3.3.1",
        "setuptools==75.6.0",
        "shellingham==1.5.4",
        "sniffio==1.3.1",
        "SQLAlchemy==2.0.36",
        "sqlmodel==0.0.22",
        "starlette==0.41.3",
        "sympy==1.13.1",
        "threadpoolctl==3.5.0",
        "tokenizers==0.21.0",
        "torch==2.5.1",
        "tqdm==4.67.1",
        "transformers==4.47.0",
        "typer==0.15.1",
        "typing_extensions==4.12.2",
        "urllib3==2.2.3",
        "uvicorn==0.34.0",
        "uvloop==0.21.0",
        "watchfiles==1.0.3",
        "websockets==14.1",
    ],
    extras_require={
        "dev": ["pytest>=7.0", "twine>=4.0.2"],
    },
    python_requires="==3.12.8",
)
