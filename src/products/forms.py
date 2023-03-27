from django.shortcuts import render, redirect

# from .forms import ProductForm


from django import forms
from .models import Product

input_css_class = "form-control"


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "handle", "price"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['name'].widget.attrs['placeholder'] = "Your name"
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = input_css_class


# def create_product(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('product_list')
#     else:
#         form = ProductForm()
#     return render(request, 'create_product.html', {'form': form})
