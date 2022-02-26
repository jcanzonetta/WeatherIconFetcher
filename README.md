# WeatherIconFetcher

Given an icon description and icon size, this program will return the file path to the requested weather icon.

Icons provided by icon8. Please follow their licenseing requirements if used: https://icons8.com/license

How to run:
Update request.json so that the following two parameters are provided:
  1. "description" [string] - Specifies the icon. Must be one of the following:
                              "sun", "storm", "snow-storm", "snow", "sleet", "rain-cloud", "rain", "partly-cloudy-day", "moon-and-stars", "light-snow", "hail", "fog"
 
  2. "size" [int]   - Specifies the size of the icon. Allowed values:
                      24, 48, 96
response.txt will be updated with the path to the request file. If for any reason the request is invalid, response.txt will be populated with "False".
