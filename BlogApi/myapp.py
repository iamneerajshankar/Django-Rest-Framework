import requests
import json

URL = "http://127.0.0.1:8000/student-info/"


def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    r = requests.get(url=URL, data=json_data)
    data = r.json()
    print(data)


def send_data():
    python_data = {
        'name': 'Ankit Sinha',
        'course': 'Mechanical Engineering',
        'roll': 201923,
        'admission_date': '2022-03-10'
    }
    json_data = json.dumps(python_data)
    send_request = requests.post(url=URL, data=json_data)
    data = send_request.json()
    print("The received response from server")
    print(data)


def update_data():
    python_data = {
        'id': 4,
        'course': 'Civil Services Preparation',
        'roll': 202019
    }
    json_data = json.dumps(python_data)
    update_request = requests.put(url=URL, data=json_data)
    data = update_request.json()
    print("The response from the server")
    print(data)


def delete_data():
    python_data = {
        'id': 4
    }
    json_data = json.dumps(python_data)

    delete_request = requests.delete(url=URL, data=json_data)
    data = delete_request.json()
    print("The response received from server")
    print(data)


# driver code
get_data()
# send_data()
# update_data()
# delete_data()
