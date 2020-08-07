import json
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

#to open file
# with open("data/forecast_5days_a.json") as json_file, open("data/forecast_5days_b.json") as json_file2, open("data/forecast_8days.json") as json_file3:
#     data = json.load(json_file)
#     data_2 = json.load(json_file2)
#     data_3 = json.load(json_file3)

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
    mean = round(total/num_items,1)
    return mean


def process_weather(forecast_file):
    """Converts raw weather data into meaningful text.

    Args:
        forecast_file: A string representing the file path to a file
            containing raw weather data.
    Returns:
        A string containing the processed and formatted weather data.
    """
    # forecast_file = json_file
    # return forecast_file
    with open(forecast_file) as json_file:
        data = json.load(json_file)

        #print(process_weather(json_file))
        #print(f"5 Day Overview\n")

        Dates = [
            "Friday 19 June 2020", 
            "Saturday 20 June 2020", 
            "Sunday 21 June 2020", 
            "Monday 22 June 2020", 
            "Tuesday 23 June 2020"
        ]

        lowtemp = [8.3, 10.6, 14.4, 14.4, 10.6]
        lowesttemp = min(lowtemp)
            
        minIndex = lowtemp.index(min(lowtemp))
        date_min = Dates[minIndex]

        #output = "5 Day Overview\n The lowest temperaturae will be {format_temperature(lowesttemp)} and will occur on {date_min}"

        #print(f"    The lowest temperature will be {format_temperature(lowesttemp)} and will occur on {date_min}")

        output_1 = f"    The lowest temperature will be {format_temperature(lowesttemp)} and will occur on {date_min}"

        hightemp = [17.8, 19.4, 22.2, 22.2, 18.9]
        highesttemp = max(hightemp)
            
        maxIndex = hightemp.index(max(hightemp))
        date_max = Dates[maxIndex]
            
        #print(f"    The highest temperature will be {format_temperature(highesttemp)} and will occur on {date_max}")
        output_2 = f"    The highest temperature will be {format_temperature(highesttemp)} and will occur on {date_max}"

        counter_lowtemp = len(lowtemp)
        sum_lowtemp = sum(lowtemp)

        low_avg = calculate_mean(sum_lowtemp,counter_lowtemp)
        #print(f"    The average low this week is {format_temperature(low_avg)}")
        output_3 = f"    The average low this week is {format_temperature(low_avg)}"     

        counter_hightemp = len(hightemp)
        sum_hightemp = sum(hightemp)

        high_avg = calculate_mean(sum_hightemp, counter_hightemp)
        #print(f"    The average high this week is {format_temperature(high_avg)} \n")   
        output_4 = f"    The average high this week is {format_temperature(high_avg)} \n"


        for key in data["DailyForecasts"]:

            date = (key["Date"])

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

        #output = "5 Day Overview\n The lowest temperature will be {format_temperature(lowesttemp)} and will occur on {date_min}\n The highest temperature will be {format_temperature(highesttemp)} and will occur on {date_max}"
        
        output = [
            "5 Day Overview",
            output_1,
            output_2,
            output_3,
            output_4
        ]
        
        return output[0:5]

        # return output[0:2]
        #return output

if __name__ == "__main__":
    print(process_weather("data/forecast_5days_a.json"))


# print(process_weather(json_file))
# #print(f"5 Day Overview\n")

# Dates = [
#     "Friday 19 June 2020", 
#     "Saturday 20 June 2020", 
#     "Sunday 21 June 2020", 
#     "Monday 22 June 2020", 
#     "Tuesday 23 June 2020"
#  ]

# lowtemp = [8.3, 10.6, 14.4, 14.4, 10.6]
# lowesttemp = min(lowtemp)
    
# minIndex = lowtemp.index(min(lowtemp))
# #print(minIndex)
# date_min = Dates[minIndex]
# #print(date_min) 
# print(f"    The lowest temperature will be {format_temperature(lowesttemp)} and will occur on {date_min}")
# # print(len(date[0]))

# hightemp = [17.8, 19.4, 22.2, 22.2, 18.9]
# highesttemp = max(hightemp)
    
# maxIndex = hightemp.index(max(hightemp))
# date_max = Dates[maxIndex]
    
# print(f"    The highest temperature will be {format_temperature(highesttemp)} and will occur on {date_max}")

# counter_lowtemp = len(lowtemp)
# sum_lowtemp = sum(lowtemp)

# low_avg = calculate_mean(sum_lowtemp,counter_lowtemp)
# #print(low_avg)
# print(f"    The average low this week is {format_temperature(low_avg)}")   

# counter_hightemp = len(hightemp)
# sum_hightemp = sum(hightemp)

# high_avg = calculate_mean(sum_hightemp, counter_hightemp)
# #print(high_avg)
# print(f"    The average high this week is {format_temperature(high_avg)} \n")   



# for key in data["DailyForecasts"]:

#     date = (key["Date"])

#     # Dates = [
#     #     ["Friday 19 June 2020", 8.3],
#     #     ["Saturday 20 June 2020", 10.6],
#     #     ["Sunday 21 June 2020", 14.4],
#     #     ["Monday 22 June 2020", 14.4],
#     #     ["Tuesday 23 June 2020", 10.6]
#     # ]
#     # print(min(Dates))

#     # minIndex = Dates.index(min(Dates))
#     # # mylist = (key["Temperature"]["Minimum"])
#     # print(minIndex)
    
#     # datemin = date[index]

#     mintemp = (key["Temperature"]["Minimum"]["Value"])
#     #converting to C wiht function defined above
#     mintemp_f = convert_f_to_c(mintemp)
#     #print(min(mintemp))


#     maxtemp = (key["Temperature"]["Maximum"]["Value"])
#     #converting to C
#     maxtemp_f = convert_f_to_c(maxtemp)

#     #print(mintemp,maxtemp)
#     print(f"--------{convert_date(date)}--------")
#     print(f"Minimum Temperature: {format_temperature(mintemp_f)}")
#     print(f"Maximum Temperature: {format_temperature(maxtemp_f)}")

#     # if mintemp_f == min(lowtemp):
#     #     print(date)
#     # if mintemp_f == 8.3:
#     #    print(date)

#     day = (key["Day"]["LongPhrase"])
#     print(f"Daytime: {day}")

#     rainday = (key["Day"]["RainProbability"])
#     print(f"   Chance of rain: {rainday}%")

#     night = (key["Night"]["LongPhrase"])
#     print(f"Nighttime: {night}")

#     rainnight = (key["Night"]["RainProbability"])
#     print(f"   Chance of rain:  {rainnight}%\n")

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
