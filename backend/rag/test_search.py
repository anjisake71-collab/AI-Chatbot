from backend.rag.embedding_service import create_embeddings
from backend.rag.vector_store import search_documents


def test_search():

    # User's question
    query = "What is Python?"

    # Convert question into an embedding
    query_embedding = create_embeddings([query])[0]

    # Search ChromaDB
    results = search_documents(query_embedding, n_results=3)

    # Display results
    print("\nSearch Results:\n")

    for document in results["documents"][0]:
        print("----")
        print(document)


if __name__ == "__main__":
    test_search() 