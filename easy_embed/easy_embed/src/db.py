"""SQLModel-based database operations for managing embeddings.

This module provides a SQLModel implementation for storing and managing vector embeddings
in a SQLite database. It includes the core Embedding model and CRUD operations
for working with embeddings.
"""

from typing import Annotated

from fastapi import Depends
from sqlalchemy import JSON, Column
from sqlmodel import Field, Index, Session, SQLModel, create_engine, select


class Embedding(SQLModel, table=True):
    """A SQLModel class representing an embedding in a vector database.

    Attributes:
        id (int): Primary key identifier for the embedding.
        index (int): Index number of the embedding within its collection.
        doc (str): The original text document associated with this embedding.
        embedding (list[float]): The vector embedding represented as a list of floats.
        collection (str): The name of the collection this embedding belongs to.

    Notes:
        - The embedding field is stored as JSON in the database
        - The collection field is indexed for faster queries
        - There is a composite index on (collection, id) for efficient lookups
    """

    id: int = Field(primary_key=True)
    index: int
    doc: str
    embedding: list[float] = Field(sa_column=Column(JSON))
    collection: str = Field(index=True)  # Add indexed collection field

    # Create composite primary key for id and collection
    __table_args__ = (Index("idx_collection_id", "collection", "id"),)


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)


def create_db_and_tables():
    """Creates the database and tables based on SQLModel metadata."""

    SQLModel.metadata.create_all(engine)


def get_session():
    """Creates and yields a new database session using SQLAlchemy's Session class."""

    with Session(engine) as session:
        yield session


# "Dependency" for most API routes. Meaning it will generate a db session for each request
SessionDep = Annotated[Session, Depends(get_session)]


def create_embedding(
    session: Session,
    doc: str,
    embedding: list[float],
    index: int,
    collection: str,
):
    """Create a new embedding in the database.

    It first checks if an embedding with the same index and collection already exists to avoid duplicates.
    """

    existing = session.exec(
        select(Embedding).where(
            (Embedding.index == index) & (Embedding.collection == collection)
        )
    ).first()

    if existing:
        raise ValueError(
            f"Embedding with index {index} in collection {collection} already exists"
        )

    db_embedding = Embedding(
        doc=doc, embedding=embedding, index=index, collection=collection
    )
    session.add(db_embedding)
    session.commit()
    session.refresh(db_embedding)
    return db_embedding


def read_collection(session: Session, collection: str) -> list[Embedding]:
    """Retrieve all embeddings from a specific collection in order of their index."""

    result = session.exec(
        select(Embedding)
        .where(Embedding.collection == collection)
        .order_by(Embedding.index)
    ).all()

    if not result:
        raise ValueError(f"Collection {collection} not found")

    return result


def update_embedding(
    session: Session,
    index: int,
    collection: str,
    doc: str,
    embedding_values: list[float],
) -> Embedding:
    """Updates an existing embedding in the database."""

    statement = select(Embedding).where(
        (Embedding.index == index) & (Embedding.collection == collection)
    )
    db_embedding = session.exec(statement).first()
    if not db_embedding:
        raise ValueError(
            f"Embedding with index {index} in collection {collection} not found"
        )

    db_embedding.doc = doc
    db_embedding.embedding = embedding_values

    session.add(db_embedding)
    session.commit()
    session.refresh(db_embedding)
    return db_embedding


def delete_embedding(
    session: Session,
    index: int,
    collection: str,
) -> Embedding:
    """Delete an embedding from the database."""

    statement = select(Embedding).where(
        (Embedding.index == index) & (Embedding.collection == collection)
    )
    db_embedding = session.exec(statement).first()
    if not db_embedding:
        raise ValueError(
            f"Embedding with index {index} in collection {collection} not found"
        )

    session.delete(db_embedding)
    session.commit()
    return db_embedding
