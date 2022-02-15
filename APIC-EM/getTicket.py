import requests
import json

APICEM_IP = '10.215.26.122'
VERSION = 'v1'
USERNAME = 'admin'
PASSWORD = 'vnpro@149'

requests.packages.urllib3.disable_warnings()

def get_ticket(ip=APICEM_IP,ver=VERSION,uname=USERNAME,pword=PASSWORD):
    r_json = {
        "username": uname,
        "password": pword
    }
    post_url = "https://"+ip+"/api/"+ver+"/ticket"
    headers = {"Content-Type" : "application/json"}
    try:
        r=requests.post(post_url,data = json.dumps(r_json),headers = headers,verify=False) 
        r.raise_for_status()
        # #token = r.json()["response"]["serviceTicket"]
        # return {
        #     "token" : token
        # }
    except:
        print("Status: %s" %r.status_code)
        print("Response: %s" %r.text)
ticket=get_ticket()
#print(ticket)