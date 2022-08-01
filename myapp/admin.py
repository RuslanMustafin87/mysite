from typing import Tuple
from django.contrib import admin
from .models import Client, Book, Major
# Register your models here.

# admin.site.register(Client)
# admin.site.register(Major)
# admin.site.register(Book)

@admin.register(Client)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'major', 'display_books')
    fields = ('name', 'age', 'major', 'books')
    # inlines = [BooksInline]

class UserInline(admin.TabularInline):
    model = Client
    extra = 0

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('book',)

# class BooksInline(admin.TabularInline):
#     model = Book
#     extra = 0

@admin.register(Major)
class MajorAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [UserInline]

# class MajorInline(admin.TabularInline):
#     model = Major
#     extra = 0