# WeatherNow

WeatherNow is a responsive Django weather app that fetches real-time weather data from the OpenWeatherMap API. Search any city or use quick city buttons for instant forecasts. It features dynamic backgrounds, detailed weather info, and a sleek UI optimized for all devices.

## Features

- Search weather by city name
- Quick buttons for popular cities (Ahmedabad, Kitchener, Mumbai, Delhi)
- Dynamic background images based on weather conditions
- Detailed weather info: temperature, humidity, wind speed, and descriptions
- Responsive and clean user interface

## Setup & Installation

1.  **Clone the repository**

    ```bash
    git clone [https://github.com/yourusername/WeatherNow.git](https://github.com/yourusername/WeatherNow.git)
    cd WeatherNow
    ```

2.  **Create and activate a virtual environment**

    ```bash
    python -m venv venv
    source venv/bin/activate    # On Windows: venv\Scripts\activate
    ```

3.  **Install Django (and requests) if not pre-installed**

    ```bash
    pip install django requests
    ```

4.  **Replace the OpenWeatherMap API key**

    Open `views.py` and replace the placeholder API key with your own OpenWeatherMap API key.

5.  **Run the Django development server**

    ```bash
    python manage.py runserver
    ```

6.  **Open your browser**

    Visit `http://localhost:8000` to use the app.

## Usage

* Enter any city name and click **Search** to get current weather.
* Or click one of the quick city buttons (Ahmedabad, Kitchener, Mumbai, Delhi) for instant updates.



   
