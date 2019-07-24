from django.urls import path
from . import views

urlpatterns = [
    path('news/<int:news_id>/', views.NewsModelSingle.as_view(), name='get single news'),
    path('news/', views.NewsModelList.as_view(), name='get all news'),
]
