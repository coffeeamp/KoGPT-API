from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from PyKakao import KoGPT

from ChatGPT import chatbot

# Create your views here.
def home(request):
   answer = chatbot("안녕하세요")
   return render(request, 'Chatfile.html', {'answer': answer})

   
       