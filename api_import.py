import requests as rq

key = "41e24b85881b4db5b32192952231212"

url = "http://api.weatherapi.com/v1/current.json?"


info = {"q":"53.1,-0.13"}

headers = {
    "Key":key,
}

response = rq.get(url, headers=headers, params=info)
print(response.json())
print(response.status_code) ## this will indicate if the api is conneting in working(200)