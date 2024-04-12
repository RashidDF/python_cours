import json

json_str = '{"id": 235, "brand": "Nike", "qty": 84, "status": {"isForSale":true}}'

sneakers = json.loads(json_str)

print(sneakers)

json_str_1 = json.dumps(sneakers, indent=3)

print(json_str_1)
