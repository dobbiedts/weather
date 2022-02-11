import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm


def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=de621d2bc6a6fb28f991966285e01d16'
    # city = 'Lagos'

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    # To enable the form clear itself when they are done
    form = CityForm()

    cities = City.objects.all()
    
    weather_data = []

    for city in cities:

        req = requests.get(url.format(city)).json()

        city_weather = {
            'city' : city.name,
            'temprature' : req['main']['temp'],
            'description' : req['weather'][0]['description'],
            'icon' : req['weather'][0]['icon'],
        }

        weather_data.append(city_weather)

    print(weather_data)

    context = {'weather_data': weather_data, 'form': form}

    return render(request, 'weather/weather.html', context)