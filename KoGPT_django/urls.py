from django.contrib import admin
from django.urls import path, include
from chat.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chat.urls')),
]