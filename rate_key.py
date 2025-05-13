import requests
import time
url="https://api.github.com/rate_limit"
remaining = requests.get(url).json()['rate']['remaining']
if remaining==0:
    time.sleep(30)
