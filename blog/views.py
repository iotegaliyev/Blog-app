from django.shortcuts import render, redirect
from .forms import ArticleForm
from .models import Article
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('articles')
        else:
            messages.error(request, 'Invalid credentials. Please try again.')

    return render(request, 'blog/login.html')


def register_user(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('articles')

    context = {'form': form}
    return render(request, 'blog/register.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def articles(request):
    form = ArticleForm()
    user = User.objects.get(pk=request.user.id)
    # articles = Article.objects.filter(author=user)
    articles = user.article_set.all()

    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)  # Create the Article instance without saving it to the database
            article.author = request.user  # Set the author to the currently logged-in user
            article.save()
            return redirect('articles')

    context = {'form': form, 'articles': articles}
    return render(request, 'blog/articles.html', context)


@login_required(login_url='login')
def update_article(request, pk):
    article = Article.objects.get(id=pk)
    form = ArticleForm(instance=article)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles')

    context = {'form': form}
    return render(request, 'blog/update-article.html', context)


@login_required(login_url='login')
def delete_article(request, pk):
    article = Article.objects.get(id=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles')
    return render(request, 'blog/delete-article.html')
