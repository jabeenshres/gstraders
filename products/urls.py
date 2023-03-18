from django.urls import path
from products.views import (
    ProductsAddView,
    ProductsListView,
    ProductsUpdateView,
    ProductsDeleteView
)

app_name = 'products'


urlpatterns = [
    path("create/", ProductsAddView.as_view(), name='create'),
    path("list/", ProductsListView.as_view(), name='list'),
    path("update/<int:pk>/", ProductsUpdateView.as_view(), name='update'),
    path("delete/<int:pk>/", ProductsDeleteView.as_view(), name='delete'),

    # path('delete/item/<int:pk>/', delete_item, name='item-delete'),

    # path('detail/<int:pk>/', PurchaseDetailView.as_view(), name='detail'),
    # path('balance-sheet/', PurchaseBalanceSheetListView.as_view(), name='balance-sheet'),

    # path("generate-pdf/<int:pk>/", GeneratePDFView.as_view(), name="generate-pdf"),
]