from relationship_app.models import Author, Book, Library


def run_queries():
    # 1. Query all books by a specific author
    try:
        author = Author.objects.get(name="J.K. Rowling")
        books_by_author = Book.objects.filter(author=author)
        print("Books by", author.name, ":", [book.title for book in books_by_author])
    except Author.DoesNotExist:
        print("Author not found.")

    # 2. List all books in a library
    try:
        library = Library.objects.get(name="Central Library")
        books_in_library = library.books.all()
        print("Books in", library.name, ":", [book.title for book in books_in_library])
    except Library.DoesNotExist:
        print("Library not found.")

    # 3. Retrieve the librarian for a library
    try:
        library = Library.objects.get(name="Central Library")
        if hasattr(library, "librarian"):
            print("Librarian of", library.name, ":", library.librarian.name)
        else:
            print("No librarian assigned to", library.name)
    except Library.DoesNotExist:
        print("Library not found.")


if __name__ == "__main__":
    run_queries()
