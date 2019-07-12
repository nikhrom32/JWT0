from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('test-list/', views.TestModelList.as_view()),
    path('test-list/<int:user_id>/', views.TestModelPerson.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
