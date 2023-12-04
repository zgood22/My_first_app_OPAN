from flask import Blueprint, request, render_template, redirect, flash

from app.weather2 import fetch_data, display_weather

weather_routes = Blueprint("weather_routes", __name__)

@weather_routes.route("/weather/form")
def weather_form():
    print("WEATHER FORM...")
    return render_template("weather_form.html")

@weather_routes.route("/weather/dashboard", methods=["GET", "POST"])
def weather_dashboard():
    print("WEATHER DASHBOARD... ")

    if request.method == "POST":
        # for data sent via POST request, form inputs are in request.form:
        request_data = dict(request.form)
        print("FORM DATA:", request_data)
    else:
        # for data sent via GET request, url params are in request.args
        request_data = dict(request.args)
        print("URL PARAMS:", request_data)

    zip_code = request_data.get("zip_code") or "90274"
    
    try:
        parsed_response, empty_var = fetch_data(zip_code=zip_code, country_code="US")
        daytime_periods = display_weather(parsed_response)
        today_temp = daytime_periods[0]['temperature']
        today_detail = daytime_periods[0]['shortForecast']
    
        flash("Fetched Real-time Market Data!", "success")
        return render_template("weather_dashboard.html",
            zip_code=zip_code,
            today_temp=today_temp,
            today_detail=today_detail
        )
    except Exception as err:
        print('OOPS', err)
       

