from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from PyKakao import KoGPT

# Create your views here.
def home(request):
   answer = "abcd"
   return render(request, 'Chatfile.html', {'answer': answer})

   
       