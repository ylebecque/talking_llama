# Chat avec local SLM avec Phi3 mini  et RAG avec Langchain, Ollama, Chroma et Streamlit

Ce projet a pour but d'aider à développer à un agent conversationnel s'appuyant sur une base de connaissance locale construite sur un corpus de textes, interrogé via une base de données vectorielle supportée par Chroma.

## Prérequis

Vous devez disposer d'une d'un serveur local Ollama disposant du model Phi3 mini. Pour cela : 
Téléchargez ollama à cette adresse : https://ollama.com/
Lancez l'appli Ollama qui créera un serveur local.
Installez alors le SLM phi3 mini depuis le terminal:
```
ollama pull phi3:mini
```
## Utilisation
Lancez l'application principale avec la commande :
```
streamlit run chat.py
```
Cette application fonctionnelle peut être utilisée pour poser des questions concernant l'IA, les LLM et plus précisément Ollama et Langchain, qui ne font pas partie des données d'entraînement de Phi3, grâce une base de données vectorielle.
## Personnalisation du modèle
Il est tout à fait possible de modifier ce modèle de chat en utilisant ses propres données.
Pour cela il suffit d’ajouter ses propres documents et de recréer une base de données.
### Ajout de fichiers
Faites glisser les documents au format markdown (.md) dans le dossier *docs*
Si vous disposez de fichiers texte bruts (.txt), il vous suffit de modifier l’extension en .md pour qu’ils soient pris en charge.
### Génération de la base de données vectorielle
Pour générer la base de données vectorielle, lancez la commande suivante depuis le dossier *utils*: 
```
python make_vdb.py
```
### Modification des instructions du modèle
Pour donner de nouvelles instructions au modèle, il vous suffit de modifier le fichier *instructions.txt* du dossier *instructions*.
