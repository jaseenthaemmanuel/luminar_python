
from django.urls import path
from base.views import *

urlpatterns = [
    path('', lambda request:render(request,"base/index.html"), name="home"),
    path('login/', login, name="login"),
    path('register/', register, name="register"),
    path('view/', lambda request:render(request, "base/view.html")),
]