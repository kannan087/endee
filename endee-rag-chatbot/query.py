from utils.embeddings import get_embedding
from endee import Client
import openai

openai.api_key = "YOUR_API_KEY"

client = Client()
collection = client.get_collection("documents")

def ask_question(query):
    query_emb = get_embedding(query)

    results = collection.query(
        query_embeddings=[query_emb],
        n_results=2
    )

    context = " ".join(results["documents"][0])

    prompt = f"Answer using context: {context} \nQuestion: {query}"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response['choices'][0]['message']['content']

if __name__ == "__main__":
    while True:
        q = input("Ask: ")
        print(ask_question(q))
