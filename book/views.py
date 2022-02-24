from django.http import Http404
from django.shortcuts import render, get_object_or_404
from . import models


def book_all(request):
    books = models.Book.objects.all()
    return render(request, 'book_list.html', {'books': books})


# hw2
def book_detail(request, id):
    try:
        book = get_object_or_404(models.Book, id=id)
        # comment
        try:
            comment = models.BookComment.objects.filter(book_id=id).order_by('created_date')
        except models.Book.DoesNotExist:
            print('No comment')
    except models.Book.DoesNotExist:
        raise Http404('Book does not exist')
    return render(request, 'books_detail.html', {'book': book})

