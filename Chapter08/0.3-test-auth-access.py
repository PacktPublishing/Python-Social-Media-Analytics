import requests

access_token = ''


### Pinterest API connection

def pinterest(url = '', params = ''):

	response = requests.get(url = url, params = params)

	print(response, response.reason)

	return response.json()


me = pinterest(url = 'https://api.pinterest.com/v1/me', params = {'access_token': access_token})

print(me)
