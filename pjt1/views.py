
from django.shortcuts import render, redirect
from .models import Review

# Create your views here.

def index(request):
    pjts = Review.objects.all()
    context = {
        'pjts': pjts
    }
    return render(request, 'pjt1/index.html', context)

def new(request):

    return render(request, 'pjt1/new.html')

def create(request):
    title = request.GET.get('create-title')
    content = request.GET.get('content')

    Review.objects.create(
        title = title,
        content = content,
    )
    
    return redirect('pjt1:index')
    # return render(request, 'pjt1/create.html')

# def new(request):
#     return render(request, 'pjt1/new.html')

def delete(request, pk):
    review = Review.objects.get(pk = pk)
    review.delete()

    return redirect('pjt1:index')

def update(request, pk):
    review = Review.objects.get(pk = pk)
    review.delete()

    return redirect('pjt1:index')

def detail(request, pk):
    pjts = Review.objects.get(pk = pk)
    context = {
        'pjts' : pjts
    }

    return render(request, 'pjt1/detail.html', context)

def edit(request, pk):
    pjts = Review.objects.get(pk = pk)
    context = {
        'pjts' : pjts
    }
    return render(request, 'pjt1/edit.html', context)   

def edit_method(request, pk):
    pjts = Review.objects.get(pk = pk)
    title = request.GET.get('update-title')
    content = request.GET.get('update-content')
    print(title, content)
    pjts.title = title
    pjts.content = content
    pjts.save()
    return redirect('pjt1:index')
