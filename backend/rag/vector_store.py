import chromadb


# Create a persistent ChromaDB client
chroma_client = chromadb.PersistentClient(
    path="./chroma_db"
)


# Create or get our collection
collection = chroma_client.get_or_create_collection(
    name="ai_chatbot_documents"
)


def add_documents(chunks, embeddings):

    documents = []
    ids = []

    for index, chunk in enumerate(chunks):

        documents.append(chunk.page_content)
        ids.append(f"chunk_{index}")

    collection.add(
        documents=documents,
        embeddings=embeddings.tolist(),
        ids=ids
    )


def search_documents(
    query_embedding,
    n_results=3,
    distance_threshold=None
):

    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=n_results
    )

    # If no threshold is provided,
    # return all retrieved results
    if distance_threshold is None:
        return results

    # Get documents and distances
    documents = results["documents"][0]
    distances = results["distances"][0]

    # Keep only results within the distance threshold
    filtered_documents = []
    filtered_distances = []

    for document, distance in zip(
        documents,
        distances
    ):

        if distance <= distance_threshold:

            filtered_documents.append(document)
            filtered_distances.append(distance)

    return {
        "documents": [filtered_documents],
        "distances": [filtered_distances]
    } 