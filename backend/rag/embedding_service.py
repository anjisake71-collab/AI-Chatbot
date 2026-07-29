from sentence_transformers import SentenceTransformer

# Use the already downloaded local Hugging Face cache
MODEL_PATH = r"C:\Users\91939\.cache\huggingface\hub\models--sentence-transformers--all-MiniLM-L6-v2\snapshots\1110a243fdf4706b3f48f1d95db1a4f5529b4d41"

embedding_model = SentenceTransformer(
    MODEL_PATH,
    local_files_only=True
)


def create_embeddings(texts):
    """
    Convert text into numerical vector embeddings.
    """
    return embedding_model.encode(
        texts,
        convert_to_numpy=True
    ) 