from django.urls import path
from modules.module_average import views

urlpatterns = [
    path('get/', views.ViewAverage.as_view()),
]