# Local RAG — Wyrd Wiki

A fully local Retrieval-Augmented Generation (RAG) system that answers questions about the Wyrd company wiki without any per-query cost.

--- 

## 🚀 Stack

- Ollama (local LLM + embeddings)
- LlamaIndex
- ChromaDB
- Python

---

## ✅ Features

- Fully local inference
- Semantic search over company wiki
- Lightweight and RAM-friendly
- Simple CLI interface
- Zero API cost

---

## 🧠 Models Used

- Embeddings: `nomic-embed-text`
- LLM: `gemma:2b`

---

## 📂 Project Structure
```
LocalRAG-Wyrd/
│
├── rag.py
├── writeup.txt
└── data/
└── wyrd_wiki.txt
```

---

## ▶️ How to Run

### 1. Install dependencies

pip install llama-index chromadb ollama

### 2. Pull Ollama models


ollama pull nomic-embed-text
ollama pull gemma:2b

### 3. Run

python rag.py

Then ask questions in the terminal.

---

## ⚠️ Notes

Designed for local execution

Performance depends on available RAM

No external API required

---

### Author: Akshay Sharma
