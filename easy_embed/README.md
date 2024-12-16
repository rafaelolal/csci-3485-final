# Easy Embed

Simple self-hosted semantic search API.

## Installation
```bash
pip install easy-embed
```

## Usage

```py
from easy_embed import App

app = App()
# optional
# app.set_model(**kwargs)
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