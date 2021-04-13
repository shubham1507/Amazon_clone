from django.contrib import admin
from django.urls import path
from An_app import views
from An_app import AdminView
from django.conf.urls.static import static

from Amazon import settings

urlpatterns = [
    path('admin/', views.adminLogin, name="admin_login"),
    path('demo', views.demoPage),
    path('demoPage', views.demoPageTemplate),
    path('admin_login_process', views.adminLoginProcess,
         name="admin_login_process"),
    path('admin_logout_process', views.adminLogoutProcess,
         name="admin_logout_process"),

    # PAGE FOR ADMIN
    path('admin_home', AdminView.admin_home, name="admin_home"),

    # CATEGORIES
    path('category_list', AdminView.CategoriesListView.as_view(),
         name="category_list"),
    path('category_create', AdminView.CategoriesCreate.as_view(),
         name="category_create"),
    path('category_update/<slug:pk>',
         AdminView.CategoriesUpdate.as_view(), name="category_update"),

    # SUBCATEGORIES

    path('sub_category_list', AdminView.SubCategoriesListView.as_view(),
         name="sub_category_list"),
    path('sub_category_create', AdminView.SubCategoriesCreate.as_view(),
         name="sub_category_create"),
    path('sub_category_update/<slug:pk>',
         AdminView.SubCategoriesUpdate.as_view(), name="sub_category_update"),

    # Merchant User
    path('merchant_create', AdminView.MerchantUserCreateView.as_view(),
         name="merchant_create"),
    path('merchant_list', AdminView.MerchantUserListView.as_view(),
         name="merchant_list"),
    path('merchant_update/<slug:pk>',
         AdminView.MerchantUserUpdateView.as_view(), name="merchant_update"),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
