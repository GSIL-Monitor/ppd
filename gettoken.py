import json

import requests

data = {
    "access_key": 'ta3gzb9lovq424zrgzkl0o13jqc4f7yd',
    "sign": "9DAF21F50797DCBC9B643B7B306188C0",
    "time": '1499767733.013236'
}

resp = requests.post(url='http://openapi-test.billbear.cn/core/v1/token',headers={'Content-Type': 'application/json', },
                     json=data)

resp_obj = json.loads(resp.text)

print(resp_obj)