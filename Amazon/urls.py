
# from django.contrib import admin
# from django.urls import path
# from An_app.views import demoPage,demoPageTemplate,adminLogin
# from django.conf.urls.static import static
# from An_app import AdminView
# from Amazon import settings

# urlpatterns = [
#     path('admin/', adminLogin),
#     path('demo/', demoPage),
#     path('demoT/', demoPageTemplate),
#     path('admin_home/', AdminView.admin_home),
# ]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)


from django.contrib import admin
from django.urls import path
from An_app import views

from An_app import AdminView
from django.conf.urls.static import static

from Amazon import settings

urlpatterns = [
    path('admin/', views.adminLogin,name="admin_login"),
    path('demo',views.demoPage),
    path('demoPage',views.demoPageTemplate),
    path('admin_login_process',views.adminLoginProcess,name="admin_login_process"),
    path('admin_logout_process',views.adminLogoutProcess,name="admin_logout_process"),

    # PAGE FOR ADMIN
    path('admin_home',AdminView.admin_home,name="admin_home")
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
