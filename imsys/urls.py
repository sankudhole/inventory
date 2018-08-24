from django.conf.urls import url
from imsys import views

app_name = 'imsys'

urlpatterns = [
    url('register/', views.register, name='register'),
    url('dashboard/', views.dashboard, name='dashboard'),
    url('logout/', views.user_logout, name='logout'),
    url('editprofile/', views.edit, name='editprofile'),
    url('salesorder/', views.saledorder, name='salesorder'),
    url('purchaseorder/', views.purchaseorder, name='purchaseorder'),
    url('', views.user_login, name='home'),
]
