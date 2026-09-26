import requests
import json

response = requests.get(
    'https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow'
)

for i, data in enumerate(response.json()['items']):
    if data['answer_count'] == 0:
        print(f"Questions:  {i}  {data['title']}")
        print(f"link:   {data['link']}")
    else:
        print("skipped")
    
    print("")        
    