import requests

code = '' ### this is what you got in previous script
app_id = '' ### app details
app_secret = '' ### app details


url = 'https://api.pinterest.com/v1/oauth/token'

params = {
    'grant_type' : 'authorization_code',
    'client_id' : app_id,
    'client_secret' : app_secret,
    'code' : code
    }

response = requests.post(url, params = params)


print(response, response.reason)


data = response.text	### contains access token
print(data)
