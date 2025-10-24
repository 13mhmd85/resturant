from django.urls import path
from django.conf.urls.static import static
from . import views
from django.conf import settings


urlpatterns = [
    path('',views.home,name='home'),
    path('detail/<id>',views.detail,name='detail'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)