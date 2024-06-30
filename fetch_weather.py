##########################################################
#                                                        #
#       fetch_weather.py                                 #
#       Fetches weather data from the National           #
#       Weather Service API and sends it to              #
#       parse_weather.py to be combed through            #
#                                                        #
#       Created by Beau Smith                            #
#                                                        #
##########################################################

import requests

def fetch_forecast(latitude, longitude):

    # constucts API URL using given coordinates
    url = f"https://api.weather.gov/points/{latitude},{longitude}"
    response = requests.get(url)
    
    # checks if site request was successful
    if response.status_code == 200:

        # converts response data to JSON
        data = response.json()

        # finds and extracts the actual forecast URL
        forecast_url = data['properties']['forecast']
        
        # attempts to fetch forecast data from the newly obtained URL
        forecast_response = requests.get(forecast_url)

        # if the program successfully got the forecast data
        if forecast_response.status_code == 200:

            # return the forecast data as a JSON file
            return forecast_response.json()
        
        else:

            # if the coordinates were deemed to be valid, but the URL doesn't lead to valid
            # forecast data, the most likely reason is that there is simply no forecast data
            # for the given coordinates
            print(f"Failed to fetch forecast data from {forecast_url}. Status code: {forecast_response.status_code}")
    
    else:

        # prints error message if fetching location URL failed
        print(f"Failed to fetch coordinates data for {latitude},{longitude}. Status code: {response.status_code}. This may indicate that forecast data is unavailable for the provided coordinates.")
    
    # returns None if either fetch fails
    return None
