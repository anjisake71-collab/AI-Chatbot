from backend.rag.embedding_service import create_embeddings
from backend.rag.vector_store import search_documents


def retrieve_context(
    query: str,
    n_results: int = 3,
    distance_threshold: float = 1.0
) -> str:

    # Convert the user's question into an embedding
    query_embedding = create_embeddings([query])[0]

    # Search ChromaDB
    results = search_documents(
        query_embedding,
        n_results=n_results
    )

    # Get documents and distances
    documents = results["documents"][0]
    distances = results["distances"][0]

    # Keep only relevant documents
    filtered_documents = []

    for document, distance in zip(documents, distances):

        if distance <= distance_threshold:
            filtered_documents.append(document)

    # If nothing relevant was found
    if not filtered_documents:
        return "No relevant information was found in the knowledge base."

    # Combine documents
    context = "\n\n".join(filtered_documents)

    return context 