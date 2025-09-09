# 1️⃣ Set up Django environment BEFORE importing models
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

# 2️⃣ Now import models
from relationship_app.models import Author, Book, Library, Librarian

# 3️⃣ Sample queries

# Query all books by a specific author
author = Author.objects.get(name="J.K. Rowling")
books_by_author = Book.objects.filter(author=author)
print("Books by J.K. Rowling:", [book.title for book in books_by_author])

# List all books in a library
library = Library.objects.get(name="Central Library")
books_in_library = library.books.all()
print("Books in Central Library:", [book.title for book in books_in_library])

# Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)
print("Librarian of Central Library:", librarian.name)
