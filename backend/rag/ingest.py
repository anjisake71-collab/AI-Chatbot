from backend.rag.text_splitter import split_documents
from backend.rag.embedding_service import create_embeddings
from backend.rag.vector_store import add_documents


def ingest_documents():

    # Step 1: Load and split documents
    chunks = split_documents()

    # Step 2: Get text from each chunk
    texts = [chunk.page_content for chunk in chunks]

    # Step 3: Create embeddings
    embeddings = create_embeddings(texts)

    # Step 4: Store chunks and embeddings in ChromaDB
    add_documents(chunks, embeddings)

    print(f"Successfully stored {len(chunks)} chunks in ChromaDB")


if __name__ == "__main__":
    ingest_documents() 