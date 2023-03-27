from django.shortcuts import redirect, render

from .models import Product

from .forms import ProductForm


def product_create_view(request):
    context = {}
    form = ProductForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        if request.user.is_authenticated:
            obj.user = request.user
            obj.save()
            return redirect(obj.get_manage_url())
        form.add_error(None, "Your must be logged in to create products.")
    context["form"] = form
    return render(request, "products/create.html", context)


def product_list_view(request):
    object_list = Product.objects.all()
    return render(request, "products/list.html", {"object_list": object_list})