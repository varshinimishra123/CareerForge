from app.services.vector_store import collection
from app.services.embedding_model import model


def find_similar_jobs(
    resume_text: str,
    top_k: int = 5
):

    query_embedding = model.encode(
        resume_text
    ).tolist()

    results = collection.query(
        query_embeddings=[
            query_embedding
        ],
        n_results=top_k
    )

    return results