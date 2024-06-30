##########################################################
#                                                        #
#       index.py                                         #
#       Program entry point, takes coordinates and uses  #
#       included methods to create simple HTML           #
#       forecast                                         #
#                                                        #
#       Created by Beau Smith                            #
#                                                        #
##########################################################

import argparse
from fetch_weather import fetch_forecast
from parse_weather import parse_forecast
from generate_html import generate_html
from coordinates_validator import validate_coordinates

def main(latitude, longitude):

    # validates the provided coordinates
    valid_latitude, valid_longitude = validate_coordinates(latitude, longitude)
    
    # prints error message if coordinates are not valid
    if valid_latitude is None or valid_longitude is None:
        print("The submitted values are invalid. Please provide valid coordinate values.")
        return
    
    # fetches weather forecast using given (now confirmed valid) coordinates
    forecast_data = fetch_forecast(valid_latitude, valid_longitude)
    
    # if the forecast data was fetched and parsed successfully
    if forecast_data:

        # write the parsed forecast data into forecast.txt
        output_file = "forecast.txt"
        parse_forecast(forecast_data, output_file)
        
        # generate an HTML file using forecast.txt
        input_file = "forecast.txt"
        output_html_file = "weather_forecast.html"
        generate_html(input_file, output_html_file)
        
        # print a conformation message if the HTML file was generated
        print(f"HTML file '{output_html_file}' generated successfully.")

    else:

        # if the forecast data was NOT fetched and parsed successfully
        print("Failed to fetch forecast data. Exiting.")

if __name__ == "__main__":
    
    # parse command-line arguments for latitude and longitude
    parser = argparse.ArgumentParser(description='Generate weather forecast HTML page based on coordinates.')
    parser.add_argument('latitude', type=str, help='Latitude of the location (between -90 and 90)')
    parser.add_argument('longitude', type=str, help='Longitude of the location (between -180 and 180)')
    
    args = parser.parse_args()
    
    # call the main function with parsed latitude and longitude arguments
    main(args.latitude, args.longitude)
