# Easy Embed App

Simple self-hosted semantic search API.

GitHub: https://github.com/rafaelolal/csci-3485-final

Demo: https://github.com/rafaelolal/csci-3485-final/blob/main/CSCI_3485_Final_Project_Presentation.pptx

## Installation
```bash
pip install easy-embed-rafaelolal
```

## Usage

```py
from easy_embed import App

app = App()

# Optional: set a SentenceTransformer model by passing in whatever necessary
# arguments
# app.set_model(**kwargs)
# 
# Optional: set device
# app.set_model_device(my_device)
#
# Optional: models that require further setup before being used can be
# accessed through `app.model`
# app.model.prepare()
#
# Optional: for models with unique encoding functions, you can override
# `app.encode` with `custom_encode` using default parameters and custom logic
# app.encode = lambda text, new = "hi": app.model.transform(text, new)

app.run(host="0.0.0.0", port=8000, allow_origins=["*"])
```

## Documentation

### API Endpoints

Visit the `/docs` url for more information and for quick testing.

Below are example values for the response body:

#### /create

```
{
  "doc": "string",
  "index": 0,
  "collection": "string"
}
```

#### /read

Use the below values only for small and simple semantic search tasks. Consider using the `collection` value for more documents or more frequent needs.
```
{
  "q": "string",
  "docs": [
    "string"
  ],
  "k": 0
}
```

Use the below values if you have already used the `create` endpoint to precompute the embedding vectors of the documents.
```
{
  "q": "string",
  "collection": "string",
  "k": 0
}
```

#### /update

The main purpose of this endpoint is to keep the embeddings up to date with your data. Consider creating a custom script to automatically make a call to this endpoint whenever a datapoint is edited in your database.
```
{
  "index": 0,
  "collection": "string",
  "doc": "string"
}
```

#### /delete

```
{
  "index": 0,
  "collection": "string"
}
```

### Custom Embedding Model

Important note: the return type for a custom encode function must be `-> list[float] | list[list[float]]`. This is because of how the similarities are computed.

Refer to the usage example above.

## Main Dependencies

Python version: `python==3.12.8`

```
fastapi==0.115.6
sentence-transformers==3.3.1
sqlmodel==0.0.22
```

## Citations

How to publish to PyPi: https://youtu.be/5KEObONUkik

Default model used: Solatorio, Aivin V. "GISTEmbed: Guided In-sample Selection of Training Negatives for Text Embedding Fine-tuning." arXiv preprint arXiv:2402.16829 (2024).