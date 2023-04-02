from django.contrib import admin
from .models import Book


admin.site.register(Book)
# class BookAdmin(admin.ModelAdmin):
#     list_display = ['book_id', 'title', 'author', 'description',
#                     'availability', 'publisher', 'publish_Date', 'price']
