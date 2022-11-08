import requests

a = requests.get('https://swapi.dev/api/planets/4')
print(a.json())
