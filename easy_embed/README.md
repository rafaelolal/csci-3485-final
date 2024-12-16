# Easy Embed App

Simple self-hosted semantic search API.

## Installation
```bash
pip install easy-embed
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

app.run(host="0.0.0.0", port=8000)
```

## Documentation

## Citations

Default model used:

@article{solatorio2024gistembed,
    title={GISTEmbed: Guided In-sample Selection of Training Negatives for Text Embedding Fine-tuning},
    author={Aivin V. Solatorio},
    journal={arXiv preprint arXiv:2402.16829},
    year={2024},
    URL={https://arxiv.org/abs/2402.16829}
    eprint={2402.16829},
    archivePrefix={arXiv},
    primaryClass={cs.LG}
}