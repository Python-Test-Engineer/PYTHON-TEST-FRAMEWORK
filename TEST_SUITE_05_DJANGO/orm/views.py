from django.shortcuts import render

from .forms import RestaurantForm, RatingForm


# Create your views here.
def index(request):
    if request.method == "POST":
        form = RestaurantForm(request.POST or None)
        if form.is_valid():
            print(form.cleaned_data)
        else:
            return render(request, "orm/index.html", {"form": form})
    context = {"form": RestaurantForm()}
    return render(request, "index.html", context)


def rating(request):
    if request.method == "POST":
        form = RatingForm(request.POST or None)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
        else:
            return render(request, "orm/rating.html", {"form": form})
    context = {"form": RatingForm()}
    return render(request, "orm/rating.html", context)
