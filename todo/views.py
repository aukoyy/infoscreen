from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.utils import timezone
# Create your views here.

from .models import TodoModel


#TODO: update/upgrade to class based view for ListView as wll
def todoList(request):
    queryset = TodoModel.objects.all()
    context = {
        'todo_object_list': queryset
    }
    return render(request, "todo/todoList.html", context)




class TodoCreate(CreateView):
    # template_name = "todo/todomodel_form.html"
    model = TodoModel
    fields = ['name',
              'description',
              'done',
              'priority',
    ]


class TodoDetailView(DetailView):
    template_name = "todo/todomodel_detail.html"
    model = TodoModel
    # queryset = TodoModel.objects.all()

    #Following is only necessary for getting the current time field.
    #If removed the current time will disappear, but the view will otherwise work
    def get_context_data(self, **kwargs):
        context = super(TodoDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class TodoUpdate(UpdateView): #,id=none
    model = TodoModel
    fields = ['name',
              'description',
              'priority',
              'done']
    template_name_suffix = '_update_form'
    # query_pk_and_slug = self.object
    # instance = get_object_or_404(TodoModel, id=id)
    # queryset = TodoModel.objects.all()

class TodoDelete(DeleteView):
    model = TodoModel
    # success_url = reverse_lazy('todolist')
    success_url = "/todolist"
    # queryset = TodoModel.objects.all()

