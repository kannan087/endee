from utils.embeddings import get_embedding
from endee import Client

client = Client()
collection = client.get_or_create_collection("documents")

def ingest_file(file_path):
    with open(file_path, "r") as f:
        text = f.read()

    chunks = text.split("\n")

    for i, chunk in enumerate(chunks):
        emb = get_embedding(chunk)
        collection.add(
            documents=[chunk],
            embeddings=[emb],
            ids=[str(i)]
        )

    print("Data stored in Endee!")

if __name__ == "__main__":
    ingest_file("data/sample.txt")
