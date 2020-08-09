import json
import plotly.express as px

from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees and celcius symbols.
    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"

def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.
    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year
    """
    d = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    return d.strftime("%A %d %B %Y")

def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius
    Args:
        temp_in_farenheit: integer representing a temperature.
    Returns:
        An integer representing a temperature in degrees celcius.
    """
    return round((temp_in_farenheit - 32) * 5/9, 1)

def calculate_mean(total, num_items):
    """Calculates the mean.
    Args:
        total: integer representing the sum of the numbers.
        num_items: integer representing the number of items counted.
    Returns:
        An integer representing the mean of the numbers.
    """
    mean = float(total)/ num_items
    mean = round(mean,1)
    return mean

def process_weather(forecast_file):
    """Converts raw weather data into meaningful text.
    Args:
        forecast_file: A string representing the file path to a file
            containing raw weather data.
    Returns:
        A string containing the processed and formatted weather data.
    """

# creating lists
col_date = []
mintemp = []
maxtemp = []
real_feel = []
real_feel_shade = []

# reading data
with open("data/forecast_5days_a.json") as json_file:
    data = json.load(json_file)
# for loop
for key in data["DailyForecasts"]:
    #getting date
    date = key["Date"]
    # append date to the list
    col_date.append(convert_date(date))
    # temperature
    minimum_daily_temp = (key["Temperature"]["Minimum"]["Value"])
    # append to the list
    mintemp.append(convert_f_to_c(minimum_daily_temp))
    maximum_daily_temp = (key["Temperature"]["Maximum"]["Value"])
    # append to the list
    maxtemp.append(convert_f_to_c(maximum_daily_temp))
    # real feel
    minimum_realfeel_temp = (key["RealFeelTemperatureShade"]["Maximum"]["Value"])
    # append to the list
    real_feel.append(convert_f_to_c(minimum_realfeel_temp))
    minimum_realfeel_shade_temp = (key["RealFeelTemperature"]["Minimum"]["Value"])
    # append to the list
    real_feel_shade.append(convert_f_to_c(minimum_realfeel_shade_temp))
df = {
    "date": col_date,
    "minimum_daily_temp": mintemp,
    "maximum_daily_temp": maxtemp,
    "minimum_realfeel_temp": real_feel,
    "minimum_realfeel_shade_temp": real_feel_shade
}
fig = px.line(
    df, 
    y=["minimum_daily_temp", "maximum_daily_temp"], 
    x="date",
    title="Minimum and Maximum Temperature per Day"
    )
fig.show()
fig = px.line(
    df, 
    y=["minimum_daily_temp", "minimum_realfeel_temp", "minimum_realfeel_shade_temp"], 
    x="date",
    title="Minimum, Minimum “real feel”, and Minimum “real feel shade” temperatures"
    )
fig.show()