import requests
import json
import sys 
from tabulate import tabulate 

requests.packages.urllib3.disable_warnings()
#Base URL
base_url = "https://10.215.26.122/api/v1/"
def post_ticket():
    url = base_url+"ticket"


#No param here
#Body
    body = {
        "username":"admin",
        "password":"vnpro@149"
        }
    #Headers
    header = {"Content-Type":"application/json"}
    #Method
    res = requests.post(url, 
        data=json.dumps(body), 
        headers=header,
        #Verify
        verify=False
        )
    res.raise_for_status()
    # ticket = res.json()["response"]["serviceTicket"]
    # return ticket
    print(res)
getTicket = post_ticket()
print(getTicket)


device =[]
try:
    resp = getTicket.get(api="network-device") 
    status = resp.status_code 
    response_json = resp.json() 
    device = response_json["response"] 
except:                                                                                     
    print("Something wrong,cannot get network device info")
    sys.exit()

if status !=200:
    print (resp.text)
    sys.exit()

if device == []:
    print("No network device found")
    sys.exit()

device_list =[]
i=0
for item in device:
    i+=1
    device_list.append([i,item["hostname"],item["managementIpAddress"],
                        item["type"],item["instanceUuid"]])

print(tabulate(device_list, headers = ['number','hostname','ip','type','mac address'], tablefmt="rst"))