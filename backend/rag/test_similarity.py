from backend.rag.embedding_service import create_embeddings
from backend.rag.vector_store import search_documents


query = "What is Python?"

# Create embedding for the question
query_embedding = create_embeddings([query])[0]

# Search ChromaDB with distance filtering
results = search_documents(
    query_embedding,
    n_results=5,
    distance_threshold=1.0
)

print("\nFiltered Search Results:\n")

documents = results["documents"][0]
distances = results["distances"][0]

if not documents:

    print("No relevant documents found.")

else:

    for index, (document, distance) in enumerate(
        zip(documents, distances),
        start=1
    ):

        print(f"Result {index}")
        print(f"Distance: {distance}")
        print(f"Document: {document}")
        print("-" * 50) 