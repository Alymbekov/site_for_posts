from django.shortcuts import render
from django.http import HttpResponse
from .models import Post,Tag
from django.shortcuts import get_object_or_404
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.utils import (
                    ObjectDetailMixin,
                    ObjectCreateMixin,
                    ObjectUpdateMixin,
                    ObjectDeleteMixin,
                )

from .forms import TagForm,PostForm
from django.shortcuts import redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.db.models import Q
def post_list(request):
    search_query = request.GET.get('search','')

    if search_query:
        posts = Post.objects.filter(Q(title__icontains=search_query)| Q(body__icontains=search_query))

    else:
        posts = Post.objects.all()

    paginator = Paginator(posts,2)

    page_number = request.GET.get('page',1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()

    if page.has_previous():
        previus_url = '?page={}'.format(page.previous_page_number())
    else:
        previus_url = ''
    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
        'page_object':page,
        'is_paginated':is_paginated,
        'next_url': next_url,
        'previus_url':previus_url
    }

    return render(request,'blog/index.html',context=context)

class PostDetail(ObjectDetailMixin,View):
    model = Post
    template = 'blog/post_detail.html'

class PostDelete(LoginRequiredMixin,ObjectDeleteMixin,View):
    model = Post
    redirect_url = 'post_list_url'
    template = 'blog/post_delete_form.html'

    raise_exception = True

class TagDelete(LoginRequiredMixin,ObjectDeleteMixin,View):
    model = Tag
    redirect_url = 'tags_list_url'
    template = 'blog/tag_delete_form.html'

    raise_exception = True

class PostCreate(LoginRequiredMixin,ObjectCreateMixin,View):
    form_model = PostForm
    template = 'blog/post_create_form.html'
    raise_exceptions = True

class TagDetail(ObjectDetailMixin,View):
    model = Tag
    template = 'blog/tag_detail.html'

class PostUpdate(LoginRequiredMixin,ObjectUpdateMixin,View):
    model = Post
    form_model = PostForm
    template = 'blog/post_update_form.html'

    raise_exception = True

class TagCreate(LoginRequiredMixin,ObjectCreateMixin,View):
    form_model = TagForm
    template = 'blog/tag_create.html'

    raise_exceptions = True

class TagUpdate(LoginRequiredMixin,ObjectUpdateMixin,View):
    model = Tag
    form_model = TagForm
    template = 'blog/tag_update_form.html'

    raise_exceptions = True

def tags_list(request):
    tags = Tag.objects.all()
    return render(request,'blog/tags_list.html',context={'tags':tags})
