from django.urls import path
from . import views

urlpatterns = [
    #path('create', views.create),
    path('sell/<str:key>/<str:barecode_manufacturer>/<int:is_cotisant>', views.sell_food_api),
    path('create/<str:key>/<str:name>', views.create_api),
    path('get_food/<str:key>/<str:barecode_manufacturer>', views.get_food)
]
