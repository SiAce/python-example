import requests
import json

app_url = "https://steamspy.com/api.php?request=appdetails&appid=578080"
response = requests.get(app_url)
html_str = response.text

app_json = json.loads(html_str)

print(type(app_json))