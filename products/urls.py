from django.urls import path
from products.views import (
    ProductsAddView,
    ProductsListView,
    ProductsUpdateView,
    ProductsDeleteView,
    CategoryDetail,
    ProductDetail,

    CategoryAddView,
    CategoryListView,
    CategoryDeleteView,
    CategoryUpdateView,

    CategoryInSite
)

app_name = 'products'


urlpatterns = [
    path("create/", ProductsAddView.as_view(), name='create'),
    path("list/", ProductsListView.as_view(), name='list'),
    path("update/<int:pk>/", ProductsUpdateView.as_view(), name='update'),
    path("delete/<int:pk>/", ProductsDeleteView.as_view(), name='delete'),

    path("category/create/", CategoryAddView.as_view(), name='category-create'),
    path("category/list/", CategoryListView.as_view(), name='category-list'),
    path("category/update/<int:pk>/", CategoryUpdateView.as_view(), name='category-update'),
    path("category/delete/<int:pk>/", CategoryDeleteView.as_view(), name='category-delete'),
    

    path('category/<slug:slug>/', CategoryDetail.as_view(), name='category-detail'),
    path('<slug:slug>/', ProductDetail.as_view(), name='product_details'),


    path("categories/all/", CategoryInSite.as_view(), name='all-categories'),
    
    

    # path('delete/item/<int:pk>/', delete_item, name='item-delete'),

    # path('detail/<int:pk>/', PurchaseDetailView.as_view(), name='detail'),
    # path('balance-sheet/', PurchaseBalanceSheetListView.as_view(), name='balance-sheet'),

    # path("generate-pdf/<int:pk>/", GeneratePDFView.as_view(), name="generate-pdf"),
]