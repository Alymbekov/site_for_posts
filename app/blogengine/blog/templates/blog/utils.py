from django.shortcuts import render
from django.shortcuts import get_object_or_404

class ObjectDetailMixin:
    model = None
    template = None

    def get(self,request,slug):
        obj = get_object_or_404(self.model,slug__iexact=slug)
        return render(request,'blog/post_detail.html',context={self.model.__name__.lower():obj})
