from django.shortcuts import render

from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.shortcuts import get_object_or_404
import json
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.decorators import login_required

from django_tables2 import SingleTableView

from .models import Products, Category
from .forms import ProductsForm, CategoryForm
from .tables import ProductsTable, CategoryTable


"""
Products Create
"""
class ProductsAddView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    template_name = "createupdate.html"
    form_class = ProductsForm
    success_url = reverse_lazy('products:list')
    success_message = 'Form has been successfully submitted.'
    view_data_url = None
    heading = "Products"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['heading'] = "Product Create"
        ctx['list'] = 'products:list'
        return ctx

    def form_valid(self, form):
        self.object = form.save(commit=False)
        new_date = datetime.now()
        self.object.date = datetime(
            self.object.date.year,
            self.object.date.month,
            self.object.date.day,
            new_date.hour,
            new_date.minute,
            new_date.second,
            new_date.microsecond
        )
        self.object.save()
        return super().form_valid(form)

"""
Products List
"""
class ProductsListView(LoginRequiredMixin, SingleTableView):
    model = Products
    table_class = ProductsTable
    template_name = 'dashboard/tablelist/table_list.html'
    paginate_by = 10
    ordering = "-id"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = 'Products'
        context['form_path'] = 'products:create'
        context['list'] = 'products:list'
        return context


"""
Products Update
"""
class ProductsUpdateView(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    template_name = "createupdate.html"
    form_class = ProductsForm
    model = Products
    success_url = reverse_lazy('products:list')
    success_message = 'Form has been successfully updated.'
    heading = 'Products'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['heading'] = "Product Update"
        ctx['list'] = 'products:list'
        return ctx

    def form_valid(self, form):
        self.object = form.save(commit=False)
        new_date = datetime.now()
        self.object.date = datetime(
            self.object.date.year,
            self.object.date.month,
            self.object.date.day,
            new_date.hour,
            new_date.minute,
            new_date.second,
            new_date.microsecond
        )
        self.object.save()
        return super().form_valid(form)

"""
Products Delete
"""
class ProductsDeleteView(LoginRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    template_name = "delete.html"
    model = Products
    success_url = reverse_lazy('products:list')


# @login_required
# def create_popup(request):
#     form = ProductsForm(request.POST or None)
#     if form.is_valid():
#         instance = form.save()
#         return HttpResponse('<script>opener.closePopup(window, "%s", "%s", "#id_products");</script>' % (instance.pk, instance))
#     return render(request, "createupdate-products.html", {"form": form, 'heading': 'Products'})


# @login_required
# @csrf_exempt
# def get_id(request):
#     if request.is_ajax():
#         get_data = request.GET['get_data']
#         data_id = Products.objects.get(id=get_data).id
#         data = {'data_id': data_id,}
#         return HttpResponse(json.dumps(data), content_type='application/json')
    # return HttpResponse("/")


# @login_required
# def update_popup(request, pk = None):
#     instance = get_object_or_404(Products, pk=pk)
#     form = ProductsForm(request.POST or None, instance=instance)
#     if form.is_valid():
# 	    instance = form.save()	
# 	    return HttpResponse('<script>opener.closePopup(window, "%s", "%s", "#id_products");</script>' % (instance.pk, instance))
#     return render(request, "createupdate-products.html", {"form": form, 'heading': 'Products'})



class CategoryDetail(generic.DetailView):
    model = Category
    template_name = 'detail.html'


class ProductDetail(generic.DetailView):
    model = Products
    template_name = 'product_details.html'



class CategoryAddView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    template_name = "createupdate.html"
    form_class = CategoryForm
    success_url = reverse_lazy('products:category-list')
    success_message = 'Form has been successfully submitted.'
    view_data_url = None
    heading = None

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['heading'] = "Product Create"
        ctx['list'] = 'products:category-list'
        return ctx

"""
Products List
"""
class CategoryListView(LoginRequiredMixin, SingleTableView):
    model = Category
    table_class = CategoryTable
    template_name = 'dashboard/tablelist/table_list.html'
    paginate_by = 10
    ordering = "-id"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = 'Category'
        context['form_path'] = 'products:category-create'
        context['list'] = 'products:category-list'
        return context


"""
Products Update
"""
class CategoryUpdateView(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    template_name = "createupdate.html"
    form_class = CategoryForm
    model = Category
    success_url = reverse_lazy('products:category-list')
    success_message = 'Form has been successfully updated.'
    heading = 'Category'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['heading'] = "Category Update"
        ctx['list'] = 'products:category-list'
        return ctx

"""
Products Delete
"""
class CategoryDeleteView(LoginRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    template_name = "delete.html"
    model = Category
    success_url = reverse_lazy('products:category-list')


class CategoryInSite(generic.TemplateView):
    template_name = 'all_category.html'
    # ordering = "-id"

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     context['title'] = 'Category'
    #     context['form_path'] = 'products:category-create'
    #     context['list'] = 'products:category-list'
    #     return context


def search(request):
    query = request.GET.get('q')
    products = Products.objects.filter(product_name__icontains=query)

    return render(request, 'product_search.html', {'products': products})