import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"


def get_data(id=None):
    data = {}
    headers = {'content-Type':'application/json'}

    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)

    r = requests.get(url=URL,headers=headers,data=json_data)
    data = r.json()
    print(data)

#get_data()

def post_data():
    data= {
        'name':'akhil',
        'roll':112,
        'city': 'bhopal'
    }
    headers = {'content-Type':'application/json'}

    json_data = json.dumps(data)
    
    r = requests.post( url=URL,headers=headers ,data=json_data)
    data = r.json()
    print(data)
 
#post_data()

def update_data():
    data= {
        'id':4,
        'name':'abish',
        'city': 'indore'
    }
    headers = {'content-Type':'application/json'}

    json_data = json.dumps(data)
    
    r = requests.put( url=URL,headers=headers ,data=json_data)
    data = r.json()
    print(data)
 
#update_data()

def delete_data():
    data= {
        'id':4}
    headers = {'content-Type':'application/json'}

    json_data = json.dumps(data)
    
    r = requests.delete( url=URL,headers=headers ,data=json_data)
    data = r.json()
    print(data)
 
delete_data()
