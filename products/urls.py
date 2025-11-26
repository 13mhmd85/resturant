from django.urls import path
from .views import tag_detail

app_name = 'product'
urlpatterns = [
    path('tag/<slug:slug>',tag_detail, name='tag_detail'),
]