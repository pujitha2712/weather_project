# Weather Detection Website

## Project Description

This is a Django-based web application for current weather detection. The application allows users to check the current weather for a given city using data from a weather API. The project demonstrates the integration of Django with external APIs to fetch and display real-time weather information.

## Features

- Search for weather by city name.
- Displays current temperature, weather conditions, and other relevant details.
- Simple and user-friendly interface.

## Getting Started

Follow these steps to set up and run the project locally:

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Django 4.x
- An API key from OpenWeatherMap or any other weather data provider

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/pujitha2712/weather_project.git
   cd weather_project
2. **Create a virtual environment**
    ```bash
    python -m venv env
3. **Activate the virtual environment**
   ```bash
    .\env\Scripts\activate
     source env/bin/activate

4. **Install the required packagest**
    ```bash
   pip install -r requirements.txt
5. Open weather_project/settings.py and add your API key and other configuration settings as needed.
6. **Run database migrations**
    ```bash
   python manage.py migrate
7. **Start the development server**
    ```bash
    python manage.py runserver


Open your web browser and go to http://127.0.0.1:8000/ to see the application in action.

Usage
Enter the name of a city in the search box.
Click the "Get Weather" button to fetch and display the current weather information for that city.
Project Structure
weather_project/ - Main project folder
weather_app/ - Application folder containing weather-related logic
migrations/ - Database migrations
templates/ - HTML templates
views.py - Application logic
models.py - Database models
urls.py - URL routing
weather_project/ - Project configuration folder
settings.py - Settings file
urls.py - Project URL routing
manage.py - Django management script
requirements.txt - Project dependencies
Contributing
Feel free to contribute to this project by creating pull requests or opening issues.

License
This project is licensed under the MIT License. See the LICENSE file for more details.

Contact
If you have any questions or suggestions, please reach out to Pujitha D R.

### Additional Notes

1. **API Key**: Make sure to update the `settings.py` file with your API key and any other configuration related to the weather API.
2. **Requirements**: If you haven't already created a `requirements.txt`, you can generate it with `pip freeze > requirements.txt`.
3. **Templates and Static Files**: Ensure that you include any necessary HTML templates or static files in the appropriate directories within your Django app.

This README file should give users a clear understanding of your project and how to get it up and running.


   

   
    
