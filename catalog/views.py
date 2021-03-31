from django.shortcuts import render
from catalog.models import Book, Author, BookInstance, Genre
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    """View function for home page of the site"""
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_authors = Author.objects.count()
    num_genres = Genre.objects.count()
    num_instances_available = BookInstance.objects.filter(
        status__exact='a').count()

    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': num_genres,
        'num_visits': num_visits,
    }
    return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
    model = Book
    paginate_by = 10


class BookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10


class AuthorDetailView(generic.DetailView):
    model = Author


class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')
