from django.shortcuts import render
from math import ceil

from .models import Category, Post


def collections(request, category_id):
    if category_id:
        category = Category.objects.get(id=category_id)
        posts = Post.objects.filter(category=category)
    else:
        category = Category(category="Common", category_en="everything", category_image="https://s15.postimg.cc/3wrklwjfv/Untitled_drawing.png")
        posts = Post.objects.all()

    page = request.GET.get('page')

    last_page = max(0, ceil(len(posts) / 6) - 1)  # Number of Pages available

    # Default next and previous pages links
    next_page = '/category/{}/?page=1'.format(category_id)
    prev_page = None

    start_index = 0
    end_index = 10

    if page:
        page = int(page)  # Interpret parameter as integer

        # query starting and ending indexes
        start_index = page * 6
        end_index = start_index + 6
        if last_page:
            if page >= last_page:
                prev_page = '/category/{}/?page={}'.format(category_id, max(0, last_page - 1))
                next_page = None
            else:
                prev_page = '/category/{}/?page={}'.format(category_id, page - 1)
                next_page = '/category/{}/?page={}'.format(category_id, page + 1)
    if not last_page:
        next_page = None

    posts = posts[start_index:end_index]

    return render(request, 'feeds/collection.html', {
        'posts': posts,
        'category_image': category.category_image,
        'next_page': next_page,
        'prev_page': prev_page,
        'page_title': 'Important {} news in India and Ceylon in Tamil'.format(category.category_en),
        'page_keywords': '{}, latest, hot, india, Lanka, Tamil'.format(category.category_en),
        'page_desc': 'Hot, Latest and important news about {} in India and Ceylon'.format(category.category_en),
    })


def document(request, post_id):
    post = Post.objects.get(id=post_id)
    # category = post.category
    sections = post.section_set.all()
    if not len(sections):
        sections = None

    context = {
        'document': post,
        'sections': sections,
        'page_title': post.page_title,
        'page_keywords': '{}, latest, hot, india, Lanka, Tamil'.format(post.page_keywords),
        'page_desc': post.page_desc,
    }
    return render(request, 'feeds/document.html', context)


def home(request):
    return collections(request, 0)