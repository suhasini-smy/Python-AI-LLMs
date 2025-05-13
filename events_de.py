
import requests

def event_def():
    url ="https://api.github.com/repos/DataTalksClub/data-engineering-zoomcamp/events?page=10"
    events=[]
    
    while url:
        response = requests.get(url)
        data=response.json()
        events.extend(data) #collect all events

        url=response.links.get('next',{}).get('url')
        # below is example
        # response.links = {
        # 'next': {'url': 'https://api.github.com/next-page'}
        # }


        return events
    
events=event_def()
for event in events:
    print(event)