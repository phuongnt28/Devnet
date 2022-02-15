import requests 
import json
import tabulate

base_url = 'http://10.215.26.122/api/v1'

def post_ticket():
    url = base_url+'/ticket'
    headers = {'Content-Type':'application/json'}
    data = {
            'username':'admin',
            'password':'vnpro@149'
        }
    r = requests.post(url, headers=headers, data=json.dumps(data), verify=False)
    resp = r.json()["response"]["serviceTicket"] 
    return resp

def get_network_device():
    device = []
    headers = {'Content-Type':'application/json','x-Auth-token': post_ticket()}
    url = base_url+'/network-device'
    resp = requests.get(url, headers=headers, verify=False)
    response_json = resp.json()['response']
    device = json.dumps(response_json, indent=4)
    return(device)


if __name__ == "__main__":
    result = get_network_device()
    print(result)
