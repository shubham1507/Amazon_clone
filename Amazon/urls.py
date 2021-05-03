from django.contrib import admin
from django.urls import path
from An_app import views
from An_app import AdminView
from django.conf.urls.static import static
from django.urls import include

from Amazon import settings

urlpatterns = [
    path('admindashboard/', include("An_app.adminurls"))
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
