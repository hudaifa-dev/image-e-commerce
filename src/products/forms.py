from django.shortcuts import render, redirect
from django.forms import modelformset_factory, inlineformset_factory
# from .forms import ProductForm


from django import forms
from .models import Product, ProductAttachment

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


class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["image", 'name', 'handle', 'price']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['name'].widget.attrs['placeholder'] = "Your name"
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = input_css_class



class ProductAttachmentForm(forms.ModelForm):
    class Meta:
        model = ProductAttachment
        fields = ["file", 'name', 'is_free', 'active']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['name'].widget.attrs['placeholder'] = "Your name"
        for field in self.fields:
            if field in ['is_free', 'active']:
                continue
            self.fields[field].widget.attrs['class'] = input_css_class


ProductAttachmentModelFormSet = modelformset_factory(
    ProductAttachment,
    form=ProductAttachmentForm,
    fields = ['file', 'name','is_free', 'active'],
    extra=0,
    can_delete=True
)

ProductAttachmentInlineFormSet = inlineformset_factory(
    Product,
    ProductAttachment,
    form = ProductAttachmentForm,
    formset = ProductAttachmentModelFormSet,
    fields = ['file', 'name','is_free', 'active'],
    extra=0,
    can_delete=True
)

