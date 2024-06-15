import requests

headers = {
    'Content-Type': 'application/json',
}

data = '{"name":"dummy", "age":21, "friends":["dummy1", "dummy2", "dummy3"], "is_man":false}' 

response = requests.post('http://127.0.0.1:5000/try_rest', headers=headers, data=data)
# print(response)
response_json = response.json()
# print(response_json)
friends = response_json['response_json']['friends']
for i in friends:
    print(i)