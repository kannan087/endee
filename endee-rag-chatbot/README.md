# Endee RAG Chatbot

## 📌 Overview
This project is a Retrieval Augmented Generation (RAG) chatbot using Endee vector database.

## ⚙️ Tech Stack
- Python
- Endee (Vector DB)
- OpenAI
- Flask

## 🔄 Workflow
1. Data is converted into embeddings
2. Stored in Endee
3. Query is embedded
4. Relevant data retrieved
5. Sent to LLM for answer

## 📊 Architecture
User → Embedding → Endee → Context → LLM → Answer

## 🚀 Setup

```bash
pip install -r requirements.txt
python ingest.py
python app.py
