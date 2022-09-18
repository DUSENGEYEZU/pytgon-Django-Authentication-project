from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path('', views.login_user, name='login'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('change_password', views.change_password, name='change_password'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)