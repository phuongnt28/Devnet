from ssl import ALERT_DESCRIPTION_UNKNOWN_PSK_IDENTITY
import requests
import meraki_info
import json

def get_organizations():
    url = meraki_info.base_url + 'organizations'
    headers = {"X-Cisco-Meraki-API-Key": meraki_info.api_key}
    resp = requests.get(url, headers=headers)
    data = resp.json()
    #print(json.dumps(data, indent=4))
    return data

def create_organizations():
    url = meraki_info.base_url + 'organizations'
    headers = {"X-Cisco-Meraki-API-Key": meraki_info.api_key}
    body = {"name": "Phuongnt Devnet"}
    resp = requests.post(url, headers=headers, json=body)
    data = resp.json()
    print(json.dumps(data, indent=4))

def get_networks():
    url = meraki_info.base_url + 'organizations/578149602163692273/networks'
    headers = {"X-Cisco-Meraki-API-Key": meraki_info.api_key}
    resp = requests.get(url, headers=headers)
    data = resp.json()
    print(json.dumps(data, indent=4))

def create_networks():
    url = meraki_info.base_url + 'organizations/578149602163692273/networks'
    headers = {"X-Cisco-Meraki-API-Key": meraki_info.api_key}
    body = {"name": "Devops Engineer",
            "timeZone": "America/Los_Angeles",
            "tags": "Phuongnt",
            "notes": "Combined network for VNG Office",
            "type": "appliance"
    }
    resp = requests.post(url, headers=headers, json=body)
    data = resp.json()
    print(json.dumps(data, indent=4))

def get_inventorydevices():
    url = meraki_info.base_url + 'organizations/578149602163692273/inventoryDevices'
    headers = {"X-Cisco-Meraki-API-Key": meraki_info.api_key}
    resp = requests.get(url, headers=headers)
    data = resp.json()
    print(json.dumps(data, indent=4))

def get_organization_id():
    org_str = get_organizations()
    #print(org_str)
    org_list = org_str
    #print(org_list)
    name = "Public API Lab"
    for org in org_list:
        if org["name"] ==name:
            org_id = org["id"]
    print(org_id)
    return org_id

#get_organizations()
#create_organizations()
#get_networks()
#create_networks()
#get_inventorydevices()
get_organization_id()