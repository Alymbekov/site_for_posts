from django.shortcuts import render
from django.http import HttpResponse
from .models import Post,Tag
from django.shortcuts import get_object_or_404
from django.views.generic import View
from blog.utils import ObjectDetailMixin,ObjectCreateMixin,ObjectUpdateMixin
from .forms import TagForm,PostForm
from django.shortcuts import redirect

def post_list(request):
    posts = Post.objects.all()
    return render(request,'blog/index.html',context={'posts':posts})

class PostDetail(ObjectDetailMixin,View):
    model = Post
    template = 'blog/post_detail.html'

class PostCreate(ObjectCreateMixin,View):
    form_model = PostForm
    template = 'blog/post_create_form.html'

    # def get(self,request):
    #     form = PostForm()
    #     return render(request,'blog/post_create_form.html',context={'form':form})
    # def post(self,request):
    #     bound_form = PostForm(request.POST)
    #     if bound_form.is_valid():
    #         new_post = bound_form.save()
    #         return redirect(new_post)
    #     return render(request,'blog/post_create_form.html',context={'form':bound_form})

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
    # def get(self,request):
    #     form = TagForm()
    #     return render(request,'blog/tag_create.html',context={'form':form})
    # def post(self,request):
    #     bound_form = TagForm(request.POST)
    #     if bound_form.is_valid():
    #         new_tag = bound_form.save()
    #         return redirect(new_tag)
    #     return render(request,'blog/tag_create.html',context={'form':bound_form})
class TagUpdate(ObjectUpdateMixin,View):
    model = Tag
    form_model = TagForm
    template = 'blog/tag_update_form.html'

def tags_list(request):
    tags = Tag.objects.all()
    return render(request,'blog/tags_list.html',context={'tags':tags})
