from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from .form import New

def read(request):
    blogs = Blog.objects
    blog_list=Blog.objects.all()
    paginator = Paginator(blog_list,9)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'read.html', {'blogs' : blogs, 'posts':posts}) 

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html', {'detail':details})

def create(request):
    if request.method == 'POST': 
        form = New(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save() 
            return redirect('read')
    else:
        form = New()
        return render(request, 'create.html', {'form':form})

def update(request, blog_id):
    post = get_object_or_404(Blog, pk = blog_id)
    form = New(request.POST, request.FILES, instance = post)
    if form.is_valid():
        form.save()
        return redirect('read')
    return render(request, 'create.html', {'form':form})

def delete(request, blog_id):
    post = get_object_or_404(Blog, pk = blog_id)
    post.delete()
    return redirect('read')
