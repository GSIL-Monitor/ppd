
import requests

url = 'http://wirelessgateway.ppdai.com/Auth/AuthService/Login'

data = {
	"extrainfo": {
		"app_feature": "AppStore_1392",
		"app_channelsid": "1392"
	},
	"LoginSource": 1,
	"UserName": "13774275220",
	'Password':'qwe123'
	# "Password": "E3myl7uWnOM\/7dENxdeSDG4a\/LP78K4ZGqHTfBX3FvZ9zBjwzZYmrIEeE49UlZOCR0sAfJephQZCoORaNx2hThrLc3KHsmhhWmk0UF9CJmE\/oNhGZ\/Dc\/re9wT5NJX5xLpj9BRqLuUUvOkAtfxdEJUrmTSBo5jKMf1zAoRneWAU="
	}

r = requests.post(url,json=data)

print(r.status_code)