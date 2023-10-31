from django.views.generic import TemplateView, ListView
from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre

def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count()
    num_genres=Genre.objects.count()
    num_search=SearchResultsView()
    return render(
        request,
        'index.html',
        context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors, 'num_genres':num_genres},
    )

class SearchResultsView(ListView):
    model = Book
    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Book.objects.filter(
            (title__icontains=query)
        )