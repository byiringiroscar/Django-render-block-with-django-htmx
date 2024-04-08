from django.shortcuts import render
from core.models import Book
from core.forms import BookForm
from render_block import render_block_to_string
from django.http import HttpResponse

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            context = {
                'form': BookForm(),
                'books': Book.objects.all()
            }
        else:
            context = {
                'form': form,
                'books': Book.objects.all()
            }
        html = render_block_to_string('index.html', 'add-book-form', context)
        return HttpResponse(html)
    context = {
        'books': Book.objects.all(),
        'form': BookForm()
    }
    return render(request, 'index.html', context)