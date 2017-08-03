

import requests




app_id = ''	###  App ID: value to find in your app details page


url = 'https://api.pinterest.com/oauth/'

params = {
    'response_type' : 'code',
    'redirect_uri' : 'https://localhost/',
    'client_id' : app_id,
    'scope' : 'read_public, read_relationships',
    'state' : '111aBc'	### any value
    }


response = requests.get(url, params = params)

print(response, response.reason)

data = response.url

print(data)

##### paste value of data into your browser
