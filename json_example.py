import requests
import json

def json_from_url(app_url):

    # app_url = "https://steamspy.com/api.php?request=appdetails&appid=578080"
    response = requests.get(app_url)
    html_str = response.text

    app_json = json.loads(html_str)

    return app_json
