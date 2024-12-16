from fastapi import FastAPI, HTTPException
from numpy import ndarray
from torch import Tensor, topk
from torch.nn.functional import cosine_similarity

from .db import (
    Embedding,
    SessionDep,
    create_db_and_tables,
    create_embedding,
    delete_embedding,
    read_collection,
    update_embedding,
)
from .main import App
from .schemas import CreateRequest, DeleteRequest, ReadRequest, UpdateRequest

api = FastAPI()
app = App()


@api.on_event("startup")
def on_startup():
    create_db_and_tables()


@api.post("/create")
def create_api(request: CreateRequest, session: SessionDep) -> dict:
    try:
        created = create_embedding(
            session=session,
            doc=request.doc,
            embedding=tolist(app.model.encode(request.doc)),
            index=request.index,
            collection=request.collection,
        )

        if created:
            return {
                "status": "success",
            }

        else:
            raise HTTPException(
                status_code=500, detail="Failed to create embedding"
            )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@api.post("/read")
def read_api(request: ReadRequest, session: SessionDep) -> dict:
    # try:
    if request.docs and request.collection:
        raise HTTPException(
            status_code=400,
            detail="Only one of 'docs' or 'collection' should be provided",
        )

    search = []
    if request.docs:
        search = enumerate(request.docs)
    if request.collection:
        search = (
            (db_embedding.index, db_embedding.doc)
            for db_embedding in read_collection(session, request.collection)
        )

    if not search:
        raise HTTPException(status_code=400, detail="No documents to search")

    q = app.model.encode(request.q, convert_to_tensor=True)
    docs = app.model.encode(
        [item[1] for item in search], convert_to_tensor=True
    )
    similarities = cosine_similarity(q.unsqueeze(0), docs, dim=-1)
    scores, indices = topk(similarities, min(request.k, len(docs)))

    return {
        "scores": tolist(scores),
        "indices": [item[0] for item in search],
    }


# except Exception as e:
#     raise HTTPException(status_code=500, detail=str(e))


@api.put("/update")
def update_api(
    update_data: UpdateRequest,
    session: SessionDep,
) -> dict:
    try:
        updated = update_embedding(
            session,
            index=update_data.index,
            collection=update_data.collection,
            doc=update_data.doc,
            embedding_values=tolist(app.model.encode(update_data.doc)),
        )

        if updated:
            return {
                "status": "success",
            }

        else:
            raise HTTPException(
                status_code=500, detail="Failed to update embedding"
            )

    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@api.put("/delete")
def delete_api(
    delete_data: DeleteRequest,
    session: SessionDep,
) -> Embedding:
    try:
        deleted = delete_embedding(
            session,
            index=delete_data.index,
            collection=delete_data.collection,
        )

        return deleted

    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def tolist(data: Tensor | ndarray) -> list:
    if isinstance(data, Tensor):
        return data.cpu().numpy().tolist()

    elif isinstance(data, ndarray):
        return data.tolist()

    raise ValueError("Data should be a Tensor or a numpy array.")
