import requests
url = 'https://api.github.com/user'
data = requests.get(url).json()
print(data)

