from backend.services.rag_service import retrieve_context


def test_rag_retrieval():

    query = "What is Python?"

    context = retrieve_context(query)

    print("\nRetrieved Context:\n")
    print(context)


if __name__ == "__main__":
    test_rag_retrieval() 