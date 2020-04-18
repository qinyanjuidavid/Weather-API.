from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
import requests
from myapp.models import Place
from myapp.forms import PlaceForm


def Home(request):
    if request.method=="POST":
        form=PlaceForm(request.POST or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form=PlaceForm()
    url="https://api.openweathermap.org/data/2.5/weather?q={}&appid=641e9a72b3808cb7a40125207c614277"
    actual_data=[]
    cities=Place.objects.all().order_by("-timestamp")
    for city in cities:
        r=requests.get(url.format(city)).json()
        weather_data={
        'city': city.city,
        "temperature": r["main"]['temp'],
        "description": r["weather"][0]["description"],
        "icon": r["weather"][0]["icon"],
        }
        actual_data.append(weather_data)

    print(actual_data)
    context={
    'form':form,
    'weather':actual_data
    }
    return render(request,'myapp/home.html',context)
