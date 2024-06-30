##########################################################
#                                                        #
#       generate_html.py                                 #
#       Uses forecast data from forecast.txt (created    #
#       by parse_weather.py) to create simple HTML file  #
#       containing the forecast in a structured table    #
#       format                                           #
#                                                        #
#       Created by Beau Smith                            #
#                                                        #
##########################################################

def generate_html(input_file, output_html_file):

    # opens text file containing forecast details
    with open(input_file, 'r') as f:
        lines = f.readlines()

    # constructs HTML with basic structure, styling, etc.
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Weather Forecast - &copy; Beau Smith</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                padding: 20px;
                color: #333;
            }}
            h1 {{
                color: #446688;
            }}
            p {{
                color: #778899;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin-bottom: 20px;
            }}
            th, td {{
                border: 1px solid #ddd;
                padding: 15px;
                text-align: left;
            }}
            th {{
                background-color: #446688;
                color: #fff;
            }}
            tr:nth-child(even) {{
                background-color: #f2f2f2;
            }}
        </style>
    </head>
    <body>
        <h1>Weather Forecast</h1>
        <p>Generated on: {}</p>
        <table>
            <tr>
                <th>Date/Time</th>
                <th>Temperature</th>
                <th>Forecast</th>
            </tr>

    # gets third line from text file for generated datetime        
    """.format(lines[2].strip()) 

    # iterates through text file, fills table with forecast data
    for i in range(3, len(lines), 1):

        # ensures there are enough
        #  lines left to process
        if i+4 < len(lines): 
            date = lines[i].strip()
            time = lines[i+1].strip()
            date_time = f"{date} {time}"
            temperature_line = lines[i+2].strip()
            forecast_line = lines[i+3].strip()
            
            # appends new row to table with date, time, temperature, and forecast
            if ": " in temperature_line and ": " in forecast_line:
                temperature = temperature_line.split(": ")[1]
                forecast = forecast_line.split(": ")[1]
                html_content += """
                    <tr>
                        <td>{}</td>
                        <td>{}</td>
                        <td>{}</td>
                    </tr>
                """.format(date_time, temperature, forecast)

    # completes HTML content and adds copyright footer            
    html_content += """
        </table>
        <footer>
            <p>Copyright &copy; Beau Smith. All rights reserved.</p>
        </footer>
    </body>
    </html>
    """

    # writes constructed HTML content to output HTML file
    with open(output_html_file, 'w') as f:
        f.write(html_content)
