import pandas as pd
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os

df = pd.read_csv("Base_Connaissances_RAG_Club_Mecatronique.csv")
embeddings = OllamaEmbeddings(model="mxbai-embed-large")

db_location = "./chrome_langchain.db"
add_documents = not os.path.exists(db_location)

if add_documents:
    documents =[]
    ids = []
    
    for i,row in df.iterrows():
        document = Document(
            page_content= row["Questions"] +" "+row["Answers"],
            id = str(i)
        )
        ids.append(str(i))
        documents.append(document)

vector_store  =Chroma(
    collection_name="About_mechatronics",
    persist_directory=db_location,
    embedding_function=embeddings
)

if add_documents:
    vector_store.add_documents(documents=documents,ids=ids)

retriever = vector_store.as_retriever(
    search_kwargs = {"k":3}
)