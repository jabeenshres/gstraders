import django_tables2 as tables

from .models import Products


class ProductsTable(tables.Table):
    edit = tables.TemplateColumn(
        template_name='dashboard/tablelist/edit_button.html',
        extra_context={
            "link": "products:update"
        }
    )
    delete = tables.TemplateColumn(
        template_name='dashboard/tablelist/delete_button.html',
        extra_context={
            "link": "products:delete"
        }
    )
    class Meta:
        model = Products
        template_name = "django_tables2/bootstrap4.html"
        exclude = (
            "id",
        )
        attrs = {
            'class': 'table table-striped table-bordered mb-0',
            'thead' : {'class': 'thead-dark', },
        }
        orderable = False
