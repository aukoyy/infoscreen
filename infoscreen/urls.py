"""infoscreen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from display.views import (
    displaypage,
)

from todo.views import (
    #Main view
    todoList,

    #Todolist views
    ListCreate,

    #Todoitem views
    TodoCreate,
    TodoDetailView,
    TodoUpdate,
    TodoDelete,
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', displaypage),


    #Handle todolists
    url(r'^todolist/createlist', ListCreate.as_view()),

    #Handle todoitems
    url(r'^todolist/$', todoList),
    url(r'^todolist/create/$', TodoCreate.as_view()),
    url(r'^todolist/(?P<pk>[-\w]+)/$', TodoDetailView.as_view()),
    url(r'^todolist/(?P<pk>\w+)/update/$', TodoUpdate.as_view()),
    url(r'^todolist/(?P<pk>\w+)/delete/$', TodoDelete.as_view()),

]
