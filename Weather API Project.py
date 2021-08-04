# File: CIS245 Weather API Project(Final)
# Name: Kevin Daugherty
# Date: 8/3/2021

import requests

print('\nWelcome to the Python Weather Service!')

def main():
    while True:
        name_zip = input('\nEnter a city name or zip code or type "Done" to exit the service: ').title()
        if name_zip == "Done":
            print('\nThank you for using the Python Weather Service. Goodbye.')
            quit()
        if name_zip.isnumeric():
            try:
                api = 'API key'                    # Enter your API key here
                url = 'https://api.openweathermap.org/data/2.5/weather?q={},us&units=imperial&appid={}'.format(name_zip, api)
                response = requests.get(url)
                x = response.json()
                v = x["main"]
                w = x["weather"]
                y = x['coord']
                z = x['wind']
                current_temperature = v['temp']
                current_high_tmep = v['temp_max']
                current_low_temp = v['temp_min']
                current_wind_speed = z['speed']
                current_pressure = v['pressure']
                current_latitude = y['lat']
                current_longitude = y['lon']
                current_humidity = v['humidity']
                weather_description = w[0]['description']
                print("\n\tConnection established...")
                print('\tDisplaying current weather data for zip code "{}":'.format(name_zip))
                print('\n\t\tTemperature = {} degree(s) Fahrenheit'.format(current_temperature))
                print('\t\tHigh Temperature : {} degree(s) Fahrenheit'.format(current_high_tmep))
                print('\t\tLow Temperature : {} degree(s) Fahrenheit'.format(current_low_temp))
                print('\t\tWind Speed : {} m/s'.format(current_wind_speed))
                print('\t\tPressure : {} hPa'.format(current_pressure))
                print('\t\tLatitude : {}'.format(current_latitude))
                print('\t\tLongitude : {}'.format(current_longitude))
                print('\t\tHumidity : {} %'.format(current_humidity))
                print('\t\tDescription : {}'.format(weather_description))
            except:
                print('\n\tUnable to establish a connection... \n\t"{}" does not appear to be a valid location.'.format(name_zip))
                question = input('\nDo you want to attempt another search? Type Yes or No: ').title()
                while question not in ('Yes', 'No'):
                    print('\n"{}" is not an avaiable option...'.format(question))
                    question = input('\nDo you want to attempt another search? Type Yes or No: ').title()
                if question == 'Yes':
                    main()
                else:
                    print("\nThank you for using the Python Weather Service. Goodbye.")
                    quit()
        else:
            try:
                api = 'API key'                       # Enter your API key here
                name_zip.replace(' ', '+')
                url = 'https://api.openweathermap.org/data/2.5/weather?q={},us&units=imperial&appid={}'.format(name_zip, api)
                response = requests.get(url)
                x = response.json()
                v = x["main"]
                w = x["weather"]
                y = x['coord']
                z = x['wind']
                current_temperature = v['temp']
                current_high_tmep = v['temp_max']
                current_low_temp = v['temp_min']
                current_wind_speed = z['speed']
                current_pressure = v['pressure']
                current_latitude = y['lat']
                current_longitude = y['lon']
                current_humidity = v['humidity']
                weather_description = w[0]['description']
                print("\n\tConnection established...")
                print('\tDisplaying current weather data for the city of "{}":'.format(name_zip))
                print('\n\t\tTemperature = {} degree(s) Fahrenheit'.format(current_temperature))
                print('\t\tHigh Temperature : {} degree(s) Fahrenheit'.format(current_high_tmep))
                print('\t\tLow Temperature : {} degree(s) Fahrenheit'.format(current_low_temp))
                print('\t\tWind Speed : {} m/s'.format(current_wind_speed))
                print('\t\tPressure : {} hPa'.format(current_pressure))
                print('\t\tLatitude : {}'.format(current_latitude))
                print('\t\tLongitude : {}'.format(current_longitude))
                print('\t\tHumidity : {} %'.format(current_humidity))
                print('\t\tDescription : {}'.format(weather_description))
            except:
                print('\n\tUnable to establish a connection... \n\t"{}" does not appear to be a valid location.'.format(name_zip))
                question = input('\nDo you want to attempt another search? Type Yes or No: ').title()
                while question not in ('Yes', 'No'):
                    print('\n"{}" is not an avaiable option...'.format(question))
                    question = input('\nDo you want to attempt another search? Type Yes or No: ').title()
                if question == 'Yes':
                    main()
                else:
                    print("\nThank you for using the Python Weather Service. Goodbye.")
                    quit()
main()