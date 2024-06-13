import openai
import pandas as pd
import shutil

from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, Document
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

CONF = 0.3

embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")
database = Chroma(persist_directory="./database", embedding_function = embeddings)

def add_db(csv_file):
    # data = pd.read_csv(csv_file, encoding='utf-8')
    target = []
    tmp = csv_file[0]
    file = tmp.split(',')
    for tmp in file:
        print(tmp)
        result = database.similarity_search_with_score(tmp, k = 1)
        if round(result[0][1], 2) >= CONF:
            target.append(tmp)

    doc = [Document(page_content= QA, metadata = {'구분': '기타'}) for QA in target]
    if len(doc) >= 1:
        database.add_documents(doc)
    return 

def searchdb():
    embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")
    database = Chroma(persist_directory="./database", embedding_function = embeddings)
    data = database.get()
    data = pd.DataFrame(data)
    print(data)
    return 

searchdb()