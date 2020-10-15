from django.urls import path
from . import views

urlpatterns = [
    #path('create', views.create),
    path('sell/<str:barecode_manufacturer>/<int:is_cotisant>', views.sell_food_api),
    path('create/<str:name>', views.create_api),
    path('get_food/<str:barecode_manufacturer>', views.get_food)
]
