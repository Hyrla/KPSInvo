from django.urls import path
from . import views

urlpatterns = [
    #path('create', views.create),
    path('sell', views.sell_food_api),
    path('create/<str:name>', views.create_api),
]
