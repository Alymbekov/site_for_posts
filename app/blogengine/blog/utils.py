from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect


class ObjectDetailMixin:
    model = None
    template = None

    def get(self,request,slug):
        obj = get_object_or_404(self.model,slug__iexact=slug)
        return render(request,self.template,context={self.model.__name__.lower():obj})


class ObjectCreateMixin:
    form_model = None
    template = None

    def get(self,request):
        form = self.form_model()
        return render(request,self.template,context={'form':form})

    def post(self,request):
        bound_form = self.form_model(request.POST)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request,self.template,context={'form':bound_form})

class ObjectUpdateMixin:
    model = None
    template = None
    form_model = None
    def get(self,request,slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.form_model(instance=obj)
        return render(request,self.template,context={'form':bound_form, self.model.__name__.lower():obj})


    def post(self,request,slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.form_model(request.POST,instance=obj)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request,self.template,context={'form':bound_form,self.model.__name__.lower():obj})