from django.shortcuts import render
from django.http import HttpResponse
from .models import Post,Tag
from django.shortcuts import get_object_or_404
from django.views.generic import View
from blog.utils import (
                    ObjectDetailMixin,
                    ObjectCreateMixin,
                    ObjectUpdateMixin,
                    ObjectDeleteMixin,
                )

from .forms import TagForm,PostForm
from django.shortcuts import redirect
from django.urls import reverse

def post_list(request):
    posts = Post.objects.all()
    return render(request,'blog/index.html',context={'posts':posts})


class PostDetail(ObjectDetailMixin,View):
    model = Post
    template = 'blog/post_detail.html'

class PostDelete(ObjectDeleteMixin,View):
    model = Post
    redirect_url = 'post_list_url'
    template = 'blog/post_delete_form.html'



class TagDelete(ObjectDeleteMixin,View):
    model = Tag
    redirect_url = 'tags_list_url'
    template = 'blog/tag_delete_form.html'



class PostCreate(ObjectCreateMixin,View):
    form_model = PostForm
    template = 'blog/post_create_form.html'


class TagDetail(ObjectDetailMixin,View):
    model = Tag
    template = 'blog/tag_detail.html'


class PostUpdate(ObjectUpdateMixin,View):
    model = Post
    form_model = PostForm
    template = 'blog/post_update_form.html'



class TagCreate(ObjectCreateMixin,View):
    form_model = TagForm
    template = 'blog/tag_create.html'


class TagUpdate(ObjectUpdateMixin,View):
    model = Tag
    form_model = TagForm
    template = 'blog/tag_update_form.html'


def tags_list(request):
    tags = Tag.objects.all()
    return render(request,'blog/tags_list.html',context={'tags':tags})
