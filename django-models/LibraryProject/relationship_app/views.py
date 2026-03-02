from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Book, Library
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# FUNCTION BASED VIEW
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_book.html", {'books': books})


# CLASS BASED VIEW
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"


# AUTHENTICATION
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, "relationship_app/member_view.html")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})


# ROLE CHECK FUNCTIONS
def is_admin(user):
    return user.userprofile.role == "Admin"


def is_librarian(user):
    return user.userprofile.role == "Librarian"


def is_member(user):
    return user.userprofile.role == "Member"


# ROLE BASED VIEWS
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")


@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")


@user_passes_test(is_member)
def member_view(request):
    return render(request, "relationship_app/member_view.html")


# CUSTOM PERMISSION VIEWS
@permission_required('relationship_app.can_add_book')
def add_book(request):
    return render(request, "relationship_app/admin_view.html")


@permission_required('relationship_app.can_change_book')
def edit_book(request):
    return render(request, "relationship_app/admin_view.html")


@permission_required('relationship_app.can_delete_book')
def delete_book(request):
    return render(request, "relationship_app/admin_view.html")

