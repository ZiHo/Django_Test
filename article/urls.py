from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name="article_list"),
    path('<int:article_id>', views.article_details, name="article_detail"),
]
