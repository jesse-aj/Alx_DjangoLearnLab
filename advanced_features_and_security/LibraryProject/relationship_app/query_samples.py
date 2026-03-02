from relationship_app.models import Author, Library, Librarian, Book


#Query all books by specific author
def books_by_author(author_name):
    # find the author instance by name
    author = Author.objects.get(name=author_name)
    # filter books using the author foreign key
    return Book.objects.filter(author=author)


#List all books in a library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()


# Retrieve librarian for a library
def librarian_of_library(library_name):
    library = Library.objects.get(name=library_name)
    # use query on Librarian model as required by checker
    return Librarian.objects.get(library=library)