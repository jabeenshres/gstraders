import django_tables2 as tables
from extras.models import HeroPage, Contact


class HeroPageTable(tables.Table):
    edit = tables.TemplateColumn(
        template_name='dashboard/tablelist/edit_button.html',
        extra_context={
            "link": "extras:hero-page-update"
        }
    )
    delete = tables.TemplateColumn(
        template_name='dashboard/tablelist/delete_button.html',
        extra_context={
            "link": "extras:hero-page-delete"
        }
    )
    class Meta:
        model = HeroPage
        template_name = "django_tables2/bootstrap4.html"
        exclude = (
            "id",
        )
        attrs = {
            'class': 'table table-striped table-bordered mb-0',
            'thead' : {'class': 'thead-dark', },
        }
        orderable = False


class ContactMessageTable(tables.Table):
    # edit = tables.TemplateColumn(
    #     template_name='dashboard/tablelist/edit_button.html',
    #     extra_context={
    #         "link": "extras:hero-page-update"
    #     }
    # )
    # delete = tables.TemplateColumn(
    #     template_name='dashboard/tablelist/delete_button.html',
    #     extra_context={
    #         "link": "extras:hero-page-delete"
    #     }
    # )
    class Meta:
        model = Contact
        template_name = "django_tables2/bootstrap4.html"
        exclude = (
            "id",
        )
        attrs = {
            'class': 'table table-striped table-bordered mb-0',
            'thead' : {'class': 'thead-dark', },
        }
        orderable = False
