
from json_example import json_from_url

def test_json_from_url():
    app_url = "https://steamspy.com/api.php?request=appdetails&appid=578080"
    json = json_from_url(app_url)

    assert json['appid'] == 578080


