from sentence_transformers import SentenceTransformer
from torch import cuda
from torch.backends import mps


class App:
    _instance = None

    def __new__(cls) -> "App":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.model = None
        return cls._instance

    def __init__(self) -> None:
        pass

    def run(self, host: str, port: int) -> None:
        if not self.model:
            self.set_model(
                **{
                    "model_name_or_path": "avsolatorio/GIST-Embedding-v0",
                    "revision": None,
                }
            )

        import uvicorn

        from .router import api

        uvicorn.run(api, host=host, port=port)

    def set_model(self, **model_kwargs: dict) -> None:
        self.model = SentenceTransformer(**model_kwargs)
        self.model.to(get_device())
        self.model.eval()
        self.model.zero_grad()
        self.model.requires_grad_(False)


def get_device() -> str:
    if cuda.is_available():
        return "cuda"
    elif mps.is_available():
        return "mps"

    return "cpu"
