# Weather Forecast HTML Generator

This Python program fetches weather forecast data based on user-provided latitude and longitude coordinates using the National Weather Service API. It then parses this data into a formatted text file and generates an HTML file displaying the forecast in a structured table format.

## Files Included

- **index.py**: Main program entry point that handles user input, coordinates validation, API data fetching, and HTML generation.
- **fetch_weather.py**: Fetches weather forecast data from the National Weather Service API.
- **parse_weather.py**: Parses forecast data into a formatted text file.
- **generate_html.py**: Generates an HTML file presenting the weather forecast in a structured table format.
- **coordinates_validator.py**: Validates latitude and longitude coordinates.
- **weather_forecast_environment.yaml**: Conda environment file to set up the required dependencies.

## Usage

1. Open a terminal or command prompt

2. Create and activate the conda environment

```
conda env create -f weather_forecast_environment.yaml

conda activate weather_app
```
3. Navigate to the directory containing the program files

4. Run the program using Python using the following format:
```
python index.py <latitude> <longitude>
```

The program will generate an HTML file (weather_forecast.html) in the same directory, which you can open in a web browser to view the weather forecast.

