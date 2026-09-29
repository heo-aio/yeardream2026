import os

import chromadb
from PyPDF2 import PdfReader
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 1. 임베디드함수 선언 + 2. 올라마 연동
embed = OllamaEmbeddings(base_url="http://localhost:11434", model="nomic-embed-text:latest")

# 3. chromadb 생성 및 collection 등록
client = chromadb.PersistentClient(path="./store")
store = Chroma(client=client, collection_name="study", embedding_function=embed)

def add_data(dir:str) -> None:
    for file in os.listdir(dir):
        print(f'{file} 읽어와 저장')
        reader = PdfReader(f'{dir}/{file}')
        text = ''
        for page in reader.pages:
            text += page.extract_text()

        text_spliter = RecursiveCharacterTextSplitter(
            chunk_size=150,
            chunk_overlap=30,
            length_function=len
        )
        docs = []
        for chunk in text_spliter.split_text(text):
            # print(chunk)
            # docs.append(Document(id='doc1', page_content=chunk, metadata={'subject':file}))
            # id 를 안넣으면 자동으로 생성해 주기에 안 넣어도 된다.
            docs.append(Document(page_content=chunk))

        store.add_documents(docs)
        print(f'{file} 저장 완료')

add_data('data')
print(store.get())