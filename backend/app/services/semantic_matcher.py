from app.services.vector_store import collection


def find_similar_jobs(
    resume_text: str,
    top_k: int = 5
):

    results = collection.query(
        query_texts=[
            resume_text
        ],
        n_results=top_k
    )

    return results