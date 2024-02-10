import datetime as dt
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from blog.models import Post, Category

NUM_POSTS = 5


def get_info(post_id=None, category_slug=None):
    if post_id is not None:
        post_detail = get_object_or_404(Post,
                                        Q(pk=post_id)
                                        & Q(pub_date__lte=dt.datetime.now())
                                        & (Q(is_published=True)
                                           & Q(category__is_published=True)))
        return post_detail
    elif category_slug is not None:
        category = get_object_or_404(Category,
                                     Q(slug=category_slug)
                                     & Q(is_published=True))
        post_list = Post.objects.filter(category_id=category.id,
                                        is_published=True,
                                        pub_date__lte=dt.datetime.now())
        return [category, post_list]
    else:
        post_list = Post.objects.filter(is_published=True,
                                        pub_date__lte=dt.datetime.now(),
                                        category__is_published=True)
        return post_list


def index(request):
    template = 'blog/index.html'
    post_list = get_info()
    context = {
        'post_list': post_list[:NUM_POSTS],
    }
    return render(request, template, context)


def post_detail(request, post_id: int):
    template = 'blog/detail.html'
    post = get_info(post_id=post_id)
    context = {
        'post': post,
    }
    return render(request, template, context)


def category_posts(request, category_slug: str):
    template = 'blog/category.html'
    category_post_list = get_info(category_slug=category_slug)
    context = {
        'category': category_post_list[0],
        'post_list': category_post_list[1],
    }
    return render(request, template, context)
