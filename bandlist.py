'''
    用json 来处理 json格式的参数
    之前用的是：params for get， data for post
'''

import requests
from pprint import pprint

url = 'http://creditpay.ppdapi.com/huanhuan/BankService/QueryUserBankCardList'

data = {"UserId":996885}

r = requests.post(url=url,json=data)
s = r.json()

print(r.status_code)
print(r.text)
print(s['Content']['CreditbankAccountsList'])
pprint(s['Content']['CreditbankAccountsList'])



url1 = 'http://creditpay.ppdapi.com/huanhuan/BankService/QueryCreditBanks'

r1 = requests.post(url=url1)
s1 = r1.json()
print(r1.status_code)