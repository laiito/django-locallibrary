from django.shortcuts import render
from catalog.models import Book, Author, BookInstance, Genre
from django.views import generic


def index(request):
    """View function for home page of the site"""
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_authors = Author.objects.count()
    num_genres = Genre.objects.count()

    num_instances_available = BookInstance.objects.filter(
        status__exact='a').count()
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': num_genres,
    }
    return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
    model = Book
    template_name = 'book_list.html'
    paginate_by = 10


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'book_detail.html'


class AuthorListView(generic.ListView):
    model = Author
    template_name = 'author_list.html'
    paginate_by = 10


class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = 'author_detail.html'
