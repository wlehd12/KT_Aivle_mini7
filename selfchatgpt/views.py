from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from .models import ChatMessage
from .models import ChatHistory
from .models import ChatgptHelpaivleqa

from langchain_community.chat_models import ChatOpenAI
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
<<<<<<< HEAD
from langchain.schema import Document

import uuid


#embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")
#database = Chroma(persist_directory="./database", embedding_function=embeddings)
=======
from langchain.chains import RetrievalQA, ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

from .function import *
import json
>>>>>>> session_test

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
    if 'chatlog' in request.session:
        del request.session['chatlog']
    return render(request, 'selfgpt/index.html')


@csrf_exempt
def chat(request):
    if request.method == "POST":
        if 'chatlog' not in request.session:
            request.session['chatlog'] = []
            memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
            chatlog = []
        else:
            chatlog = request.session['chatlog']
            memory = memory_save(chatlog)

        query = request.POST.get('question')
        user = request.user
        # 맥락 저장을 위한 conversation_id
        conversation_id = request.POST.get('conversation_id', None)
        
        # 새로운 대화가 시작될 때 기존 대화 삭제
        if not conversation_id:
            conversation_id = str(uuid.uuid4())
            ChatMessage.objects.all().delete()  # 기존 모든 대화 삭제
            
        # 최근 memory개의 대화를 기억함
        memory = 4
        previous_messages = ChatMessage.objects.filter(conversation_id=conversation_id).order_by('timestamp')[:memory]
        context = "\n".join([f"User: {msg.user_message}\nBot: {msg.bot_response}" for msg in previous_messages])
        
        full_query = f"{context}\nUser: {query}"
        
        database = getQAdb()
        
        chat = ChatOpenAI(model="gpt-3.5-turbo")
        k = 3
        retriever = database.as_retriever(search_kwargs={"k": k})
        qa = ConversationalRetrievalChain.from_llm(llm=chat, retriever=retriever, memory=memory,
                                           return_source_documents=False,  output_key="answer")
        result = qa(query)

        msg = [result['question'], result['answer']]
        chatlog.append(msg)
        request.session['chatlog'] = chatlog
        
        chat_message = ChatMessage.objects.create(user_message=query, bot_response=result["answer"])
        ChatHistory.objects.create(user=user, question=query, answer=result["answer"])
        return JsonResponse({
            'result': result["answer"],
            'timestamp': chat_message.timestamp.strftime('%Y-%m-%d %H:%M:%S')
        })
    else:
        return JsonResponse({'result': 'Invalid request'}, status=400)
    

def chat_history(request):
    messages = ChatMessage.objects.all().order_by('-timestamp')
    return render(request, 'selfgpt/chat_history.html', {'messages': messages})


@csrf_exempt
def clear_history(request):
    if request.method == "POST":
        ChatMessage.objects.all().delete()
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'fail'}, status=400)

