##########################################################
#                                                        #
#       parse_weather.py                                 #
#       Combs through forecast data and parses           #
#       date/time, temperature, and forecast             #
#       details into a text file "forecast.txt"          #
#                                                        #
#       Created by Beau Smith                            #
#                                                        #
##########################################################

from datetime import datetime

def parse_forecast(forecast_data, output_file):

    # opens output file in "write mode"
    with open(output_file, 'w') as f:

        # weather forecast header
        f.write("Weather Forecast\n")
        
        # gets and formats the date and time of forecast generation
        generated_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        f.write("Generated on:\n")
        f.write(f"{generated_datetime}\n\n")
        
        # iterates through each forecast period in the forecast data
        for period in forecast_data['properties']['periods']:

            # converts startTime to a datetime object
            start_time = datetime.fromisoformat(period['startTime'][:-6])

            # formats the newly converted startTime for the HTML file to display  
            formatted_start_time = start_time.strftime("%B %d, %Y\n%I %p").replace(":00", "").replace(" 0", " ") 
            
            # writes the date and time, temperature, and short forecast into the output file
            f.write(f"Date/Time:\n{formatted_start_time}\n")
            f.write(f"Temperature: {period['temperature']} °F\n")
            f.write(f"Forecast: {period['shortForecast']}\n")
            f.write("\n")
