import requests


weather_API = "21d27e158a6d8a6a42d48281085f0e46"
city = input('Enter city name: ')
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_API}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
    '''
    temp = data['main']['temp']
    desc = data['weather'][0]['description']
    print(f'Temp: {temp}')
    print(f'Description: {desc}')
    '''
else:
    print('Error fetching weather data.')