from django.db import models
from django.urls import reverse

# Create your models here.

class Book(models.Model):
    book = models.CharField(max_length=255)
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book", null=True)
    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])
    def __str__(self):
        return self.book
    class Meta:
        permissions = (('can_edit_book', 'Edit book'),)

class Major(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self):
        return self.title

class Client(models.Model):
    name  = models.CharField(max_length=255)
    age = models.IntegerField(null=True, blank=True)
    major = models.ForeignKey(Major, help_text="Специальность", on_delete=models.SET_NULL, null=True)
    books = models.ManyToManyField('Book', help_text='Выберите книги')
    def __str__(self):
        return self.name
    def display_books(self):
        return ', '.join([item.book for item in self.books.all()])
    def get_absolute_url(self):
        return reverse('client-detail', args=[str(self.id)])

