from django.db import models


# title, description, image, created_date,
# # updated_date, author

class Book(models.Model):
    objects = None
    title = models.CharField(max_length=40)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    created_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    author = models.CharField(max_length=20)


def __str__(self):
    return self.title


class BookDetails(models.Model):
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)


# hw2
class BookComment(models.Model):
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE,
                             related_name='books_comment')
