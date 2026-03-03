from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.llms.ollama import Ollama
from llama_index.core.node_parser import SentenceSplitter
from llama_index.vector_stores.chroma import ChromaVectorStore
import chromadb

# -------- SETTINGS --------

EMBED_MODEL = "nomic-embed-text"
LLM_MODEL = "gemma:2b"

# -------- LOAD DOCS --------

documents = SimpleDirectoryReader("./data").load_data()

# -------- CHUNKING --------

splitter = SentenceSplitter(
    chunk_size=500,
    chunk_overlap=80,
)

# -------- EMBEDDINGS --------

embed_model = OllamaEmbedding(model_name=EMBED_MODEL)

# -------- VECTOR DB --------

chroma_client = chromadb.Client()
collection = chroma_client.create_collection("wyrd_wiki")

vector_store = ChromaVectorStore(chroma_collection=collection)

# -------- LLM --------

llm = Ollama(
    model=LLM_MODEL,
    request_timeout=120.0,
    base_url="http://localhost:11434",
)

from llama_index.core import Settings
Settings.llm = llm
Settings.embed_model = embed_model

# -------- INDEX --------

index = VectorStoreIndex.from_documents(
    documents,
    transformations=[splitter],
    embed_model=embed_model,
    vector_store=vector_store,
)

query_engine = index.as_query_engine(
    similarity_top_k=4,
    llm=llm,
)

# -------- QUERY LOOP --------

print("✅ RAG ready. Ask questions. (type 'exit' to quit)")


while True:
    q = input("\nAsk: ")
    if q.lower() in ["exit", "quit"]:
        break
    response = query_engine.query(q)
    print("\nAnswer:", response)