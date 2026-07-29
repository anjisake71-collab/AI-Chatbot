from backend.rag.document_loader import load_documents


def test_document():

    documents = load_documents()

    text = documents[0].page_content

    print("\nDOCUMENT CHARACTER CHECK\n")

    checks = [
        "language known",
        "and scripting",
        "interactive web",
        "and AI",
        "allows an",
        "make decisions",
        "and perform",
        "users to",
        "images, or",
        "store and",
        "text, images",
    ]

    for phrase in checks:

        if phrase in text:
            print(f"FOUND    : {phrase}")
        else:
            print(f"NOT FOUND: {phrase}")


if __name__ == "__main__":
    test_document()  