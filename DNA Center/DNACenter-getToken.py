import requests
import json
from tabulate import tabulate

base_url = "https://sandboxdnac.cisco.com/dna/intent/api/v1/"
def post_ticket():
    url=base_url+"auth/token"

    headers={"Content-Type":"application/json",
             "Authorization":"Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE=",
    }
    res=requests.post(url,
                      headers=headers,
                      )
    data=res.json()
    print(data)
    return data
post_ticket()

def get_network_device():
    url=base_url + "network-device"
    token = post_ticket()
    #print(token["Token"])
    headers = {"Content-Type": "application/json",
                "X-Auth-Token":token["Token"]
               }
    res = requests.get(url,headers=headers)
    data = json.dumps(res.json(), indent=4)
    print(data)
    return data
get_network_device()

def creat_list_device():
    data = get_network_device()
    data = json.loads(data)
    list=[]
    for i in data["response"]:
        list.append([i["family"],i["description"],i["softwareType"]])
    headers = ["Ten thiet bi","Mo ta", "Lai"]
    print(tabulate(list, headers=headers))
creat_list_device()
