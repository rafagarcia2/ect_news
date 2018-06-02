from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, AbaPrincipal
from .forms import UploadFileForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    abas = AbaPrincipal.objects.filter(is_active=True)
    return render(request, 'blog/post_list.html', {'posts': posts, 'abas': abas})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    abas = AbaPrincipal.objects.filter(is_active=True)
    return render(request, 'blog/post_detail.html', {'post': post, 'abas': abas})

# def post_new(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.published_date = timezone.now()
#             if request.user is User:
#                 post.author = request.user
#             post.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = PostForm()
#     return render(request, 'blog/post_edit.html', {'form': form})
# Imaginary function to handle an uploaded file.


@login_required
def post_new(request):
    abas = AbaPrincipal.objects.filter(is_active=True)
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            if request.user is User:
                post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = UploadFileForm()
    return render(request, 'blog/post_edit.html', {'form': form, 'abas': abas})


@login_required
def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)
    abas = AbaPrincipal.objects.filter(is_active=True)
    if request.method == "POST":
        form = UploadFileForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = UploadFileForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form, 'abas': abas})
