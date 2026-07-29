from pathlib import Path

from langchain_core.documents import Document


def load_documents():

    # Find the project root directory
    project_root = Path(__file__).resolve().parents[2]

    # Build the path to our knowledge document
    document_path = (
        project_root
        / "documents"
        / "python_notes.txt"
    )

    # Read the text file directly
    with open(
        document_path,
        "r",
        encoding="utf-8"
    ) as file:

        text = file.read()

    # Create a LangChain Document
    document = Document(
        page_content=text,
        metadata={
            "source": str(document_path)
        }
    )

    return [document]  