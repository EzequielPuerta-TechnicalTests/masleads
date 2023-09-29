import json


def decode(response):
    return json.loads(response.data.decode("utf8"))
