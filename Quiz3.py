import requests
import json

id = 2
upperPrice = 15
url = f'https://www.cheapshark.com/api/1.0/deals?storeID={id}&upperPrice={upperPrice}'
res = requests.get(url)
res_status = res.status_code
res_header = res.headers
print(res)
#print(res.status_code)
#print(res.headers)
#res_json = res.text
#response = json.loads(res_json)
res_json = res.json()
response_structure = json.dumps(res_json, indent=4)
print(response_structure)
with open('data.json', 'w') as json_file:
    data = json.loads(response_structure)
    print("\ntitle: ", data[0]['title'])
    print("\ndeal rating: ", data[0]['dealRating'])
