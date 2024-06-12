from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

# ChatMessage 모델 가져오는 코드 추가
from .models import ChatMessage
from .models import ChatHistory

from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.chains import RetrievalQA, ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

from .function import *
import json

embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")
database = Chroma(persist_directory="./database", embedding_function=embeddings)

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

        chat = ChatOpenAI(model="gpt-3.5-turbo")
        k = 3
        retriever = database.as_retriever(search_kwargs={"k": k})
        qa = ConversationalRetrievalChain.from_llm(llm=chat, retriever=retriever, memory=memory,
                                           return_source_documents=False, output_key="answer")
        result = qa(query)

        msg = [result['question'], result['answer']]
        chatlog.append(msg)
        request.session['chatlog'] = chatlog
        print(request.session['chatlog'])
        print(result)
        
        chat_message = ChatMessage.objects.create(user_message=query, bot_response=result["answer"])
        ChatHistory.objects.create(question=query, answer=result["answer"])
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

