from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='ecommerce/index.html'), name='landing'),

    path('dashboard/', login_required(TemplateView.as_view(template_name='dashboard/dashboard.html')), name='dashboard-home'),
    path('products/', include('products.urls')),
    path('gstraders/admin/',include("accounts.urls")),

]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)