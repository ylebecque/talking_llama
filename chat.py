import streamlit as st

# Chat
from langchain_community.chat_models.ollama import ChatOllama
from langchain_core.messages import AIMessage, HumanMessage

# Historique
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

# Filtrage de l'historique
from langchain_core.runnables import RunnablePassthrough

# Prompt
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# Chromadb
import chromadb

# Ollama
import ollama

# Pathlib
from pathlib import Path

# Packages spécifiques au déploiement de l'appli sur Streamlit Cloud
__import__("pysqlite3")
import sys

sys.modules["sqlite3"] = sys.modules.pop("pysqlite3")

# Configuration de la page
st.set_page_config(
    page_title="Talking Llama",
    initial_sidebar_state="expanded",
    menu_items={
        "About": "**Repo Github** : https://github.com/ylebecque/talking_llama"
    },
)

st.header("Talking Llama")

with st.sidebar:
    logo_path = Path.cwd() / "logo" / "talking_llama.png"
    st.image(logo_path.as_posix())

# Chargement de la base de données vectorielle
path = Path.cwd() / "chromadb"
chroma_client = chromadb.PersistentClient(path.as_posix())
collection = chroma_client.get_collection(name="llm_docs")

# Création du modèle, choix de ph3 mini
model = ChatOllama(model="phi3:mini")


# Configuration du retriever
def retrieve_from_chroma(query):
    response = ollama.embeddings(prompt=query, model="nomic-embed-text:latest")
    results = collection.query(query_embeddings=[response["embedding"]], n_results=3)
    context = results["documents"][0]
    context = " ".join(context)
    return context


# Création de l'historique de messages (chatbot)
# store qui contient les messages
# config qui contient la configuration de l'historique
if "store" not in st.session_state:
    st.session_state.store = {}
else:
    store = st.session_state.store

if "config" not in st.session_state:
    st.session_state.config = {"configurable": {"session_id": "miniG"}}
else:
    config = st.session_state.config


def get_session_history(session_id: str) -> BaseChatMessageHistory:
    # Fonction qui renvoie l'historique des messages
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]


# Gestion de la fenêtre de l'historique
def filter_messages(messages, k=10):
    # Fonction qui renvoie les k derniers messages
    return messages[-k:]


def stream_response(prompt):
    # Fonction renvoyant les messages sous forme de streaming
    for word in with_message_history.stream(
        [HumanMessage(content=prompt)], config=config
    ):
        yield word


# Gestion de la personnalité et des instructions
if "instructions" not in st.session_state:
    instruct_path = Path.cwd() / "instructions" / "instructions.txt"
    try:
        with open(instruct_path) as file:
            instructions = file.read()
    except FileNotFoundError:
        st.error(
            """Fichier d'instruction 'instructions.txt' non trouvé dans le dossier 'instructions'
                 Veuillez l'ajouter dans le dossier 'instructions'.
                 Le modèle utilise une instruction par defaut."""
        )
        instructions = "Tu t'appelles Talking LLama et tu ses un assistant qui répond aux questions qu'on lui pose avec politesse et sérieux."
else:
    instructions = st.session_state.instructions

# Affichage de l'historique des messages (streamlit)
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            # "content": "Hi. I'm MiniG,I can answer questions about AI, LLM, NLP, Ollama and Langchain.",
            "content": "Bonjour. Je suis Talking Llama et je peux répondre à vos questions concernant l'IA, les LLM, Ollama et Langchain.",
        }
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Lecture du prompt de l'utilisateur
if entree := st.chat_input("Message LittleG"):
    # Affichage du message dans l'interface
    with st.chat_message("user"):
        st.markdown(entree)
    # Ajout du message dans l'historique streamlit
    st.session_state.messages.append({"role": "user", "content": entree})

    # Création du modèle de prompt

    context = retrieve_from_chroma(entree)
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f"{instructions} Utilise le contexte suivant pour repondre à la question. Contexte : {context} Question:",
            ),
            MessagesPlaceholder(variable_name="messages"),
        ]
    )

    chain = (
        RunnablePassthrough.assign(messages=lambda x: filter_messages(x["messages"]))
        | prompt
        | model
    )

    # Création de la requête
    with_message_history = RunnableWithMessageHistory(
        chain, get_session_history, input_messages_key="messages"
    )
    with st.chat_message("assistant"):
        # Création du streaming de réponse
        with st.spinner("Laissez-moi réfléchir…"):
            response = st.write_stream(
                with_message_history.stream(
                    {"messages": HumanMessage(content=entree)}, config=config
                )
            )
    # Ajout du message dans l'historique streamlit
    st.session_state.messages.append({"role": "assistant", "content": response})
