# views.py

from django.shortcuts import render, redirect
from .forms import CategoryForm, PageForm
from .models import Category, Page

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')  # Redirect to homepage after adding category
    else:
        form = CategoryForm()
    return render(request, 'add_category.html', {'form': form})

def add_page(request, category_id):
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            page = form.save(commit=False)
            page.category_id = category_id  # Assign the category_id to the page
            page.save()
            return redirect('homepage')  # Redirect to homepage after adding page
    else:
        form = PageForm()
    return render(request, 'add_page.html', {'form': form})

def display_data(request):
    categories = Category.objects.all()
    pages = Page.objects.all()
    return render(request, 'display_data.html', {'categories': categories, 'pages': pages})

# views.py


def homepage(request):
    categories = Category.objects.all()
    return render(request, 'homepage.html', {'categories': categories})
