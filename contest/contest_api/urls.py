from django.urls import path
from . import views

urlpatterns = [
    path('', views.contestList, name="contests"),
    path('<str:pk>/', views.contestDetail, name="contestDetail"),
    # path('detail/', views.detailList, name="detail"),
]