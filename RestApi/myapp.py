from datetime import date
import requests
import json

URL ="http://127.0.0.1:8000/create-Student/"
ct = date.today()
current = ct.isoformat()
data = {
    'name': 'Neeraj Shankar',
    'age': 21,
    'roll': 817161023,
    'marks': 97,
    'pass_date': current
    
}

json_data = json.dumps(data)

send_data = requests.post(url=URL, data=json_data)
extracted_data = send_data.json()
print(extracted_data)