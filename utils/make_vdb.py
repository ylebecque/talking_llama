import chromadb
import ollama
from pathlib import Path
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from tqdm import tqdm

# Chemin d'accès aux fichiers texte
path = Path.cwd().parent / "docs"
documents = []

# Chargement des fichiers
for file in path.glob("*.md"):
    loader = UnstructuredMarkdownLoader(file)
    doc = loader.load()[0]
    # Ajout de métadata sur la source
    doc.metadata["source"] = file.name
    documents.append(doc)

# Text Splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=20,
    length_function=len,
    is_separator_regex=False,
)
texts = []
for doc in documents:
    texts += text_splitter.create_documents([doc.page_content], [doc.metadata])

# Création de la base de données vectorielle et embeddings

path = Path.cwd().parent / "chromadb"
path = path.as_posix()

chroma_client = chromadb.chromadb.PersistentClient(path)

collection = chroma_client.get_or_create_collection(name="llm_docs")

docs = [text.page_content for text in texts]

for idx in tqdm(range(len(docs))):
    # for idx, doc in enumerate(docs):
    doc = docs[idx]
    response = ollama.embeddings(model="nomic-embed-text:latest", prompt=doc)
    embedding = response["embedding"]
    collection.add(
        ids=[str(idx)],
        embeddings=[embedding],
        documents=[doc],
    )
