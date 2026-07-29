from langchain_text_splitters import RecursiveCharacterTextSplitter

from backend.rag.document_loader import load_documents


def split_documents():

    # Step 1: Load the original documents
    documents = load_documents()

    # Step 2: Create the text splitter
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=30,
        length_function=len,
        is_separator_regex=False
    )

    # Step 3: Split documents into smaller chunks
    chunks = text_splitter.split_documents(documents)

    # Step 4: Return the chunks
    return chunks 