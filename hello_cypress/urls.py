from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('accounts/', include('allauth.urls')),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('form-layout/', views.form_layout, name='form-layout'),
    path('form-wizard/', views.form_wizard, name='form-wizard'),
    path('table-basic/', views.table_basic, name='table-basic'),
    path('table-advance/', views.table_advance, name='table-advance'),
    path('accounts/login', views.login, name='login'),
    path('accounts/signup', views.register, name='register'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
