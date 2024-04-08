from django.shortcuts import render
from core.models import Book
from core.forms import BookForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            context = {
                'form': BookForm()
            }
            return render(request, 'form.html', context)
        context = {
            'form': form
        }
        return render(request, 'form.html', context)
    context = {
        'books': Book.objects.all(),
        'form': BookForm()
    }
    return render(request, 'index.html', context)