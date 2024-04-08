from django.shortcuts import render
from core.models import Book
from core.forms import BookForm

# Create your views here.
def index(request):
    context = {}
    return render(request, 'index.html', context)