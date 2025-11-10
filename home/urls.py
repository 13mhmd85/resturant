from django.urls import path
from django.conf.urls.static import static
from . import views
from django.conf import settings

app_name = 'home'
urlpatterns = [
    path('',views.home,name='home'),
    path('detail/<slug:slug>',views.productdetail,name='detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)