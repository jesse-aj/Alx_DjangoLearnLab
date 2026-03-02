from django.db import models
from django.conf import settings

# AUTHOR MODEL

class Author(models.Model):
    # Stores the author's name
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# BOOK MODEL

class Book(models.Model):
    # Title of the book
    title = models.CharField(max_length=200)

    # Publication year (used in template)
    publication_year = models.IntegerField()

    # Many books to One author
    # If author is deleted, delete all their books
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="books"
    )

    #Custom Permissions
    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]

    def __str__(self):
        return self.title

# LIBRARY MODEL

class Library(models.Model):
    # Name of library
    name = models.CharField(max_length=200)

    # Many libraries ↔ Many books
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name



# LIBRARIAN MODEL

class Librarian(models.Model):
    name = models.CharField(max_length=100)

    # One librarian ↔ One library
    library = models.OneToOneField(
        Library,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name



# USER PROFILE (Role Based Access)

class UserProfile(models.Model):

    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]

    # One profile per user
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # Role field
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"
