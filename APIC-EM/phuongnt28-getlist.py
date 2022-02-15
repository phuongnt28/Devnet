import requests

#import json library
import json

#import tabulate library
from tabulate import tabulate

requests.packages.urllib3.disable_warnings()

#controller='sandboxapic.cisco.com'
controller='https://10.215.26.122/api/v1/'

def getTicket():
	# put the ip address or dns of your apic-em controller in this url
	url = controller + "ticket"

	#the username and password to access the APIC-EM Controller
	payload = {"username":"admin","password":"vnpro@149"}

	#Content type must be included in the header
	header = {"content-type": "application/json"}

	#Performs a POST on the specified url to get the service ticket
	response= requests.post(url,data=json.dumps(payload), headers=header, verify=False)

	print (response)
	
	#convert response to json format
	r_json=response.json()

	#parse the json to get the service ticket
	ticket = r_json["response"]["serviceTicket"]

	return ticket


def getNetworkDevices(ticket):
	# URL for network-device REST API call to get list of exisiting devices on the network.
	url = controller + "network-device"

	#Content type as well as the ticket must be included in the header 
	header = {"content-type": "application/json", "X-Auth-Token":ticket}

	# this statement performs a GET on the specified network device url
	response = requests.get(url, headers=header, verify=False)

	# json.dumps serializes the json into a string and allows us to
	# print the response in a 'pretty' format with indentation etc.
	print ("Network Devices = ", end="")
	print (json.dumps(response.json(), indent=4, separators=(',', ': ')))
	
	#convert data to json format.
	r_json=response.json()
	
	#Iterate through network device data and print the id and series name of each device
	
	for i in r_json["response"]:
		print(i["id"] + "     " + '{:26}'.format(i["hostname"]) + " " + '{:18}'.format(i["managementIpAddress"]) + " " + '{:45}'.format(i["series"]) + " " + i["reachabilityStatus"])
		


theTicket=getTicket()
getNetworkDevices(theTicket)