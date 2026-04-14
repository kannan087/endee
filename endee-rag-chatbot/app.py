from flask import Flask, request, jsonify
from query import ask_question

app = Flask(__name__)

@app.route("/")
def home():
    return "Endee RAG Chatbot Running!"

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    question = data.get("question")
    answer = ask_question(question)
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)
