import requests
from django.shortcuts import render
from django.conf import settings

def weather(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        api_key = settings.WEATHER_API_KEY
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            'q': city,
            'appid': api_key,
            'units': 'metric'  # Use 'imperial' for Fahrenheit
        }
        response = requests.get(base_url, params=params)
        data = response.json()
        
        if data['cod'] == 200:
            weather_data = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon']
            }
        else:
            weather_data = {'error': data['message']}
    else:
        weather_data = None

    return render(request, 'weather_app/weather.html', {'weather_data': weather_data})
