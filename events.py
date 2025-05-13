import requests
url ="https://api.github.com/repos/DataTalksClub/data-engineering-zoomcamp/events?page=10"
while True:
    response = requests.get(url)
    data=response.json()
    #print(data)
    if 'next' not in response.links:
        break
    data2 = response.links['next']['url']
    print(data2)

