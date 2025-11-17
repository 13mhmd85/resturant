from django.urls import path
from django.conf.urls.static import static
from . import views
from django.conf import settings

from .views import navbar_partial

app_name = 'home'
urlpatterns = [
    path('',views.home,name='home'),
    path('detail/<slug:slug>',views.productdetail,name='detail'),
    path('navbar',navbar_partial,name='navbar'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)