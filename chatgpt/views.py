from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django import forms
from django.urls import reverse
from django.utils import timezone

from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, AIMessage
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA, ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory , ChatMessageHistory 
from langchain.schema import Document
from .models import ChatHistory

import pandas as pd
import json

from .models import ChatgptHelpaivleqa

# Create your views here.

# Chroma 데이터베이스 초기화 - 사전에 database가 완성 되어 있다는 가정하에 진행 - aivleschool_qa.csv 내용이 저장된 상태임
# embeddings = OpenAIEmbeddings(model = "text-embedding-ada-002")
# database = Chroma(persist_directory = "./database", embedding_function = embeddings)

# DB remke
def getQAdb():
    QAdf=ChatgptHelpaivleqa.objects.all()
    embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")
    database = Chroma(persist_directory="./database", embedding_function = embeddings )
    # 각 행의 데이터를 Document 객체로 변환 
    documents = [Document(page_content=QA.qa)  for QA in QAdf]

    # 데이터프레임에서 문서 추가
    database.add_documents(documents)
    return database

database=getQAdb()

def index(request):
    return render(request, 'gpt/index.html')

def chat(request):
    #post로 받은 question (index.html에서 name속성이 question인 input태그의 value값)을 가져옴
    query = request.POST.get('question')

    #chatgpt API 및 lang chain을 사용을 위한 선언
    chat = ChatOpenAI(model="gpt-3.5-turbo")
    k = 3
    retriever = database.as_retriever(search_kwargs={"k": k})
    qa = RetrievalQA.from_llm(llm=chat,  retriever=retriever,  return_source_documents=True)

    result = qa(query)

    # result.html에서 사용할 context
    context = {
        'question': query,
        'result': result["result"]
    }
     # 질문과 응답을 ChatHistory 모델에 저장
    ChatHistory.objects.create(question=query, answer=result["result"])


    # 응답을 보여주기 위한 html 선택 (위에서 처리한 context를 함께 전달)
    return render(request, 'gpt/result.html', context) 



