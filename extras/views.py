from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django_tables2 import SingleTableView

from extras.models import HeroPage, Contact
from extras.forms import HeroPageForm, ContactForm
from extras.tables import HeroPageTable, ContactMessageTable

from products.models import Products, Category

class HomePageView(generic.TemplateView):
    template_name = "ecommerce/index.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # context["hero_pages"] = HeroPage.objects.filter(is_displayed=True)
        # context["categories"] = Category.objects.all()[0:5]
        context["products"] = Products.objects.all()
        context["products_liked"] = Products.objects.filter(is_liked=True)[::-1][0:15]

        return context

class HeroPageAddView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    template_name = "createupdate.html"
    form_class = HeroPageForm
    success_url = reverse_lazy('extras:hero-page-create')
    success_message = 'Form has been successfully submitted.'
    view_data_url = None
    heading = None

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['heading'] = "Hero Page Create"
        ctx['list'] = 'extras:hero-page-list'
        return ctx

"""
Hero Page List
"""
class HeroPageListView(LoginRequiredMixin, SingleTableView):
    model = HeroPage
    table_class = HeroPageTable
    template_name = 'dashboard/tablelist/table_list.html'
    paginate_by = 10
    ordering = "-id"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = 'HeroPage'
        context['form_path'] = 'extras:hero-page-create'
        return context


"""
Hero Page Update
"""
class HeroPageUpdateView(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    template_name = "createupdate.html"
    form_class = HeroPageForm
    model = HeroPage
    success_url = reverse_lazy('extras:hero-page-list')
    success_message = 'Form has been successfully updated.'
    heading = 'HeroPage'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['heading'] = "HeroPage Update"
        ctx['list'] = 'extras:hero-page-list'
        return ctx

"""
Hero Page Delete
"""
class HeroPageDeleteView(LoginRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    template_name = "delete.html"
    model = HeroPage
    success_url = reverse_lazy('extras:hero-page-list')



"""
Contact Create
"""

class ContactMessage(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    template_name = "contacts.html"
    form_class = ContactForm
    success_url = reverse_lazy('extras:contact-us')
    success_message = 'Form has been successfully submitted.'


class ContactListView(LoginRequiredMixin, SingleTableView):
    model = Contact
    table_class = ContactMessageTable
    template_name = 'dashboard/tablelist/table_list.html'
    paginate_by = 10
    ordering = "-id"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = 'Contact Message'
        return context