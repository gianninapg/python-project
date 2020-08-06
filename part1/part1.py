import json
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

#to open file
with open("data/forecast_5days_a.json") as json_file:
    data = json.load(json_file)

# Output:
#print(data)


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
    c = round((temp_in_farenheit-32)*5/9,1)
    return c


def calculate_mean(total, num_items):
    """Calculates the mean.
    
    Args:
        total: integer representing the sum of the numbers.
        num_items: integer representing the number of items counted.
    Returns:
        An integer representing the mean of the numbers.
    """
    pass


def process_weather(forecast_file):
    """Converts raw weather data into meaningful text.

    Args:
        forecast_file: A string representing the file path to a file
            containing raw weather data.
    Returns:
        A string containing the processed and formatted weather data.
    """
    pass

if __name__ == "__main__":
    print(process_weather("data/forecast_5days_a.json"))



for key in data["DailyForecasts"]:
    #if key == "DailyForecasts":
    #print(data["DailyForecasts"])
    

    date = (key["Date"])
    #print(date)

    mintemp = (key["Temperature"]["Minimum"]["Value"])
    #converting to C wiht function defined above
    mintemp_f = convert_f_to_c(mintemp)
    #print(min(mintemp))


    maxtemp = (key["Temperature"]["Maximum"]["Value"])
    #converting to C
    maxtemp_f = convert_f_to_c(maxtemp)

    #print(mintemp,maxtemp)
    print(f"--------{convert_date(date)}--------")
    print(f"Minimum Temperature: {format_temperature(mintemp_f)}")
    print(f"Maximum Temperature: {format_temperature(maxtemp_f)}")


    day = (key["Day"]["LongPhrase"])
    print(f"Daytime: {day}")

    rainday = (key["Day"]["RainProbability"])
    print(f"   Chance of rain: {rainday}%")

    night = (key["Night"]["LongPhrase"])
    print(f"Nighttime: {night}")

    rainnight = (key["Night"]["RainProbability"])
    print(f"   Chance of rain:  {rainnight}%\n")


    # lowest_temp = min(mintemp)
    # # print(lowest_temp)
    # print(f"{mintemp[0]} {mintemp[1]}")

    # for value in len(mintemp)
    #     print(min(value))


    # for tea_category in tea_collection:
#     #print(tea_category)
#     print(f"{tea_category[0]} Teas:")
#     for tea in tea_category[1:]:
#         print(f"     {tea}")

    lowtemp = [8.3, 10.6, 14.4, 14.4, 10.6]
    lowesttemp = min(lowtemp)
    print(lowesttemp)

    # average = (key["Temperature"]["Minimun"])
    # print(average)

    # mintemp_avg = calculate_mean(mintemp,5)
    # print(format_temperature(mintemp_avg)

    #print(mean(format_temperature(mintemp_avg))

   # str(round(average, 2))
    # average = (key["Temperature"]["Minimun"])
    # calculate_mean(["Temperature"]["Minimun"])
    
    #print(f"The average low this week is {format_temperature(mintemp_f)}")

    # print(process_weather(mintemp))
    # print(process_weather(maxtemp))
    #print(f"Minimum temerature")


    # for date in key:
    #    print(date["Date"])
    #    for value in date:
    #        print(value)

# for key in data["DailyForecasts"]:
#     #if key == "DailyForecasts":
#     #print(data["DailyForecasts"])
#     date = [key["Date"]]
#     print(date)

# """ 2 keys - Headline [0] and DailyForecasts [1]
# 5 dictionaries inside DailyForecasts List
# DailyForecasts List has 15 keys
# Date is a key of DailyForecasts List  with a value in date format
# Date is [0]
# Sun is [2]
# Temperature is [4]
# Day is [11]
# """
