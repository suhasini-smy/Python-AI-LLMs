import requests
url="https://api.github.com/repos/DataTalksClub/data-engineering-zoomcamp/events"
response = requests.get(url).json()
print(response)