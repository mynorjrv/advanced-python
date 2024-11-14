import requests

# print(requests.codes.__dict__)

reply = requests.get('http://localhost:3000')
print(reply.status_code)

if reply.status_code==requests.codes.ok:
    print('Alles gut')
    print(reply.headers['Content-Type'])
    print(reply.text)
