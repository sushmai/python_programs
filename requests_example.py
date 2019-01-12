import requests

req = requests.get("http://github.com/")
# know the type of request
print(type(req))

# print status of the request
print(req.status_code)

print(req.headers)

print(req.headers['content-type'])

print(req.text)

      
