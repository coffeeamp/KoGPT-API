from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from PyKakao import KoGPT

from ChatGPT import chatbot

# Create your views here.
def home(request):
   if request.method == 'GET':
      return render(request, 'Chatfile.html')
   else:
      text = request.POST.get('input',None)
      answer = chatbot(text)
      return render(request, 'Chatfile.html', {'answer': answer})

   
       