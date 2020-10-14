from django.shortcuts import render, HttpResponse
from .forms import ThingForm


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
