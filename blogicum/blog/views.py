import datetime as dt

from django.shortcuts import render, get_object_or_404

from blog.models import Post, Category

NUM_POSTS = 5


def get_post_info():
    return Post.objects.filter(is_published=True,
                               pub_date__lte=dt.datetime.now())


def index(request):
    template = 'blog/index.html'
    post_list = get_post_info().filter(
        category__is_published=True
    )
    context = {
        'post_list': post_list[:NUM_POSTS],
    }
    return render(request, template, context)


def post_detail(request, post_id: int):
    template = 'blog/detail.html'
    post = get_object_or_404(get_post_info().filter(
        category__is_published=True),
        pk=post_id)
    context = {
        'post': post,
    }
    return render(request, template, context)


def category_posts(request, category_slug: str):
    template = 'blog/category.html'
    category = get_object_or_404(Category,
                                 slug=category_slug,
                                 is_published=True)
    post_list = get_post_info().filter(category_id=category.id)
    context = {
        'category': category,
        'post_list': post_list,
    }
    return render(request, template, context)
