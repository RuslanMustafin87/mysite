from distutils.command.clean import clean
from django.shortcuts import render
from .models import Client, Book
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
def index(request):
    return render(request, 'index.html')

class ClientListView(generic.ListView):
    model = Client
    template_name = 'myapp/my_client_list.html'
    context_object_name = 'my_client_list'
    def get_context_data(self, **kwargs):
        context = super(ClientListView, self).get_context_data(**kwargs)
        context['clients'] = 'List of clients'
        return context

class ClientDetailView(generic.DetailView):
    model = Client
    template_name = 'myapp/client_detail.html'

class BookListView(generic.ListView):
    model = Book
    # template_name = 'myapp/my_client_list.html'
    # context_object_name = 'my_client_list'

class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'myapp/book_detail.html'

# from .forms import NewBookForm
# from django.http import HttpResponseRedirect
# from django.urls import reverse

# def new_book(request):

#     if request.method == 'POST':

#         form = NewBookForm(request.POST)

#         if form.is_valid():
#             book = Book()
#             book.book = form.cleaned_data['book']
#             book.save()

#             return HttpResponseRedirect(reverse('books') )
#     else:
#         form = NewBookForm(initial = {'title': 'New title'})

#     return render(request, 'myapp/book_new_book.html', {'form': form})

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User

class BookCreateView(PermissionRequiredMixin, CreateView):
    model = Book
    fields = '__all__'
    permission_required = 'myapp.can_edit_book'

class BookUpdateView(PermissionRequiredMixin, UpdateView):
    model = Book
    fields = '__all__'
    permission_required = 'myapp.can_edit_book'

class BookDeleteView(PermissionRequiredMixin, DeleteView):
    model = Book
    # print(reverse_lazy('books'))
    success_url = reverse_lazy('books')
    permission_required = 'myapp.can_edit_book'

class ArchitectorListView(generic.ListView):
    model = Client
    template_name = 'myapp/architector_list.html'
    context_object_name = 'architector_list'
    def get_queryset(self):
        return Client.objects.filter(major__title__iexact='architector').order_by('name')
