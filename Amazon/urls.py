
from django.contrib import admin
from django.urls import path
from An_app.views import demoPage,demoPageTemplate,adminLogin
from django.conf.urls.static import static
from An_app import AdminView
from Amazon import settings

urlpatterns = [
    path('admin/', adminLogin),
    path('demo/', demoPage),
    path('demoT/', demoPageTemplate),
    path('admin_home/', AdminView.admin_home),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)


