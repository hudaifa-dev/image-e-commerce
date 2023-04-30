import mimetypes
from django.shortcuts import get_object_or_404, redirect, render
from django.http import FileResponse, HttpResponseRedirect, HttpResponseBadRequest

from .models import Product, ProductAttachment

from .forms import ProductAttachmentInlineFormSet, ProductForm, ProductUpdateForm


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


def product_detail_view(request, handle=None):
    obj = get_object_or_404(Product, handle=handle)
    is_owner = False
    if request.user.is_authenticated:
        is_owner = obj.user = request.user
    context = {"object": obj}
    if is_owner:
        form = ProductForm(request.POST or None, instance=obj)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save
        # return redirect('/products/create/")
        context["form"] = form
    return render(request, "products/detail.html", context)


def product_attachment_download_view(request, handle=None, pk=None):
    attachment = get_object_or_404(ProductAttachment, product__handle=handle, pk=pk)
    can_download = attachment.is_free or False
    if request.user.is_authenticated:
        can_download = True  # check ownership
    if can_download is False:
        return HttpResponseBadRequest
    file = attachment.file.open(node="rb")  # In -> 53 object storage
    filename = attachment.file.name
    content_type, _ = mimetypes.guess_type(filename)
    response = FileResponse(file)
    response["Content-Type"] = content_type or "application/octet-stream"
    response["Content-Disposition"] = f"attachment;filename={filename}"
    return response


def product_manage_detail_view(request, handle=None):
    obj = get_object_or_404(Product, handle=handle)
    attachments = ProductAttachment.objects.filter(product=obj)
    is_manager = False
    if request.user.is_authenticated:
        is_manager = obj.user == request.user
    context = {"object": obj}
    if not is_manager:
        return HttpResponseBadRequest()
    form = ProductUpdateForm(request.POST or None, request.FILES or None, instance=obj)
    formset = ProductAttachmentInlineFormSet(request.POST or None, 
                                             request.FILES or None,queryset=attachments)
    if form.is_valid() and formset.is_valid():
        instance = form.save(commit=False)
        instance.save()
        formset.save(commit=False)
        for _form in formset:
            attachment_obj = _form.save(commit=False)
            attachment_obj.product  = instance
            attachment_obj.save()
        return redirect(obj.get_manage_url())
    context['form'] = form
    context['formset'] = formset
    return render(request, 'products/manager.html', context)