from app.weather2 import fetch_data
from app.weather2 import display_weather

def test_fetch_data():
    response, status = fetch_data("90274", country_code="US")
    assert isinstance(response, dict)
    assert status == 200


def test_display_weather():
    response, empty_var = fetch_data("90274", country_code="US")
    daytime_var = display_weather(response)
    assert daytime_var[0]['name'] == "This Afternoon"
    #the first response should always be "this afternoon"
    assert isinstance(daytime_var, list)