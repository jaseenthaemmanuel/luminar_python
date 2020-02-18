from django.contrib import admin
from django.urls import path
from books.views import *

urlpatterns = [
    path('',booklisting,name="booklist"),
    path('create',bookcreating,name="bookcreate"),
    path('view/<int:pk>',bookview,name='bookview'),
]
