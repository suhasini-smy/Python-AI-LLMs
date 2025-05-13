from google.colab import userdata
API_TOKEN = userdata.get('API_TOKEN')

headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

requests.get(url,headers=headers).json()