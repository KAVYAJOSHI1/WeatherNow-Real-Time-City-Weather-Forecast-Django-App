import requests
from django.shortcuts import render

def home(request):
    weather_data = None
    api_key = "55a623e7085ff87477bacfa065d5bfc7"  # ← Replace this with your actual key

    if 'city' in request.GET:
        city = request.GET['city']
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather_data = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'].title(),
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed'],
                'icon_url': f"http://openweathermap.org/img/wn/{data['weather'][0]['icon']}@2x.png"
            }
        else:
            weather_data = {
                'city': "City Not Found",
                'temperature': "-",
                'description': "Please check spelling",
                'humidity': "-",
                'wind_speed': "-",
                'icon_url': ""
            }

    return render(request, 'weather/home.html', {'weather': weather_data})
