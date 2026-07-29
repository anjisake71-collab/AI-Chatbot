from backend.services.rag_service import retrieve_context
from backend.services.groq_service import generate_rag_response


def test_rag_groq():

    question = "What is Python?"

    # Step 1: Retrieve relevant information from ChromaDB
    context = retrieve_context(question)

    print("\nRetrieved Context:\n")
    print(context)

    # Step 2: Send context + question to Groq
    answer = generate_rag_response(
        question=question,
        context=context
    )

    print("\nAI Answer:\n")
    print(answer)


if __name__ == "__main__":
    test_rag_groq() 