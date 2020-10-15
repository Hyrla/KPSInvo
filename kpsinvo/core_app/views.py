from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound
from .forms import ThingForm
from .models import Thing, Food, FoodStock, FoodSale, APIToken
from django.utils import timezone


def check_key(key):
    try:
        apitoken = APIToken.objects.find(key=key)
        if apitoken is not None:
            return True
        else:
            return False
    except APIToken.DoesNotExist:
        return False


def create_api(request, key, name, barecode_kps=None, barecode_manufacturer=None):
    if not check_key(key):
        return HttpResponse(status=403)
    thing = Thing(name=name, barecode_kps=barecode_kps, barecode_manufacturer=barecode_manufacturer)
    thing.save()
    return HttpResponse('ok')


def get_food(request, key, barecode_manufacturer):
    if not check_key(key):
        return HttpResponse(status=403)
    try:
        food = Food.objects.find(barecode_manufacturer=barecode_manufacturer)
        return HttpResponse({"name": food.name, "price": food.price, "price_cotisant": food.price_cotisant})
    except Food.DoesNotExist:
        return HttpResponseNotFound('Food not found')


def sell_food_api(request, key, barecode_manufacturer, is_cotisant):
    if not check_key(key):
        return HttpResponse(status=403)
    try:
        food = Food.objects.find(barecode_manufacturer=barecode_manufacturer)
        foodstock = FoodStock.objects.find(food=food)
        foodstock.stock -= 1
        foodstock.save()
        foodsale = FoodSale(food=food, date=timezone.now(), is_cotisant=is_cotisant == 1)
        foodsale.save()
        return HttpResponse('ok')
    except Food.DoesNotExist:
        return HttpResponseNotFound('Food not found')
    except FoodStock.DoesNotExist:
        return HttpResponseNotFound('FoodStock not found')


# Create your views here.
def create(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ThingForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            instance = form.save(commit=False)
            # do some stuff with instance
            instance.save()
            return HttpResponse('ok')
        else:
            print(form.errors.as_data())
            return HttpResponse(status=400)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ThingForm()

    return render(request, 'core_app/form.html', {'form': form})
