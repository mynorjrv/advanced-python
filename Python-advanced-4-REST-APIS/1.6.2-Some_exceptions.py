import requests

try:
    reply = requests.get('http://localhost:3000', timeout=1)
except requests.exceptions.ConnectionError:
    print('Nobody is at home')
except requests.exceptions.Timeout:
    print('Sorry, Mr. Impatient, you didnt ger our data')
else:
    print('Here is yopur data, sir')

# RequestException
# |___HTTPError
# |___ConnectionError
# |   |___ProxyError	
# |   |___SSLError	
# |___Timeout
# |   |___ConnectTimeout
# |   |___ReadTimeout
# |___URLRequired
# |___TooManyRedirects
# |___MissingSchema
# |___InvalidSchema
# |___InvalidURL
# |   |___InvalidProxyURL
# |___InvalidHeader
# |___ChunkedEncodingError
# |___ContentDecodingError
# |___StreamConsumedError
# |___RetryError
# |___UnrewindableBodyError
