from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.utils import timezone

from .models import TodoModel, TodoList


#TODO: update/upgrade to class based view for ListView as well
def todoList(request):
    todo_items = TodoModel.objects.all()
    todo_lists = TodoList.objects.all()
    context = {
        'todo_lists': todo_lists,
        'todo_items': todo_items,
    }
    return render(request, "todo/todoList.html", context)




# CRUD for todolists

class ListCreate(CreateView):
    # template_name = 'todo/todolist_form.html'
    model = TodoList
    fields = ['name',
              'description',
    ]


#TODO implement functionality for update and delete lists

# END CRUD for todolists



# CRUD For todoitems

class TodoCreate(CreateView):
    # template_name = "todo/todomodel_form.html"
    model = TodoModel
    fields = ['name',
              'description',
              'done',
              'priority',
              'todoList',
    ]


class TodoDetailView(DetailView):
    template_name = "todo/todomodel_detail.html"
    model = TodoModel
    # queryset = TodoModel.objects.all()

    #The following is only necessary for getting the current time field.
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
              'done',
              'todoList',
    ]
    template_name_suffix = '_update_form'
    # query_pk_and_slug = self.object
    # instance = get_object_or_404(TodoModel, id=id)
    # queryset = TodoModel.objects.all()

class TodoDelete(DeleteView):
    model = TodoModel
    # success_url = reverse_lazy('todolist')
    success_url = "/todolist"
    # queryset = TodoModel.objects.all()

# END CRUD for todoitems