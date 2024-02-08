import datetime
from django.http import Http404
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category

TIME_NOW = datetime.datetime.now()


def index(request):
    template = 'blog/index.html'
    post_list = Post.objects.all().filter(is_published=True,
                                          pub_date__lte=TIME_NOW,
                                          category__is_published=True)                                 
    context = {
        'post_list': post_list[:5],
    }
    return render(request, template, context)


def post_detail(request, post_id: int):
    template = 'blog/detail.html'
    post = get_object_or_404(Post,
                             Q(pk=post_id)
                             & Q(pub_date__lte=TIME_NOW)
                             & (Q(is_published=True)
                                & Q(category__is_published=True)))
    context = {
        'post': post,
    }
    return render(request, template, context)


def category_posts(request, category_slug: str):
    template = 'blog/category.html'
    category = get_object_or_404(Category,
                                 Q(slug=category_slug)
                                 & Q(is_published=True))
    post_list = Post.objects.filter(category_id=category.id,
                                    is_published=True,
                                    pub_date__lte=TIME_NOW)
    context = {
        'category': category,
        'post_list': post_list,
    }
    return render(request, template, context)
