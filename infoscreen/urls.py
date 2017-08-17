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
    displaypage_cssgrid,
    displaypage_cssgridtut,
    displaypage_cssgridtut3,
    displaypage_cssgridtut4,
)

from todo.views import (
    todoList,
    TodoCreate,
    TodoUpdate,
    TodoDelete,
    TodoDetailView,
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', displaypage),
    url(r'^grid/$', displaypage_cssgrid),
    
    
    url(r'^todolist/$', todoList),
    url(r'^todolist/create/$', TodoCreate.as_view()),
    url(r'^todolist/(?P<pk>[-\w]+)/$', TodoDetailView.as_view()),
    url(r'^todolist/(?P<pk>\w+)/update/$', TodoUpdate.as_view()),
    url(r'^todolist/(?P<pk>\w+)/delete/$', TodoDelete.as_view()),
    
    
    url(r'^gridtut/$', displaypage_cssgridtut),
    url(r'^gridtut3/$', displaypage_cssgridtut3),
    url(r'^gridtut4/$', displaypage_cssgridtut4)

]
