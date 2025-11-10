from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.user_page, name='user_page'),
    path('edit/', views.edit, name='edit'),
]