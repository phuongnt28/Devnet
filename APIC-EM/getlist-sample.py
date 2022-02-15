import requests

#import json library
import json


#import tabulate library
from tabulate import tabulate

requests.packages.urllib3.disable_warnings()

#controller APIC-EM
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

	#print (response)
	
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
	
	#convert data to json format.
	r_json=response.json()
		
	length = len(r_json["response"]) # Lấy ra số lượng thiết bị trả về (mỗi thiết bị nằm trong một list)  --> result=5 
	
	i = 0   # Tao biến đếm 

	my_table = [['ID', 'HOSTNAME', 'ManagementIpAddress', 'series', 'ReachabilityStatus']]  # Tạo list để vẽ ra bảng, mỗi hàng(row) được tính là 1 list

	while i < length:
		my_response = r_json["response"][i]  # truy vấn vào từng thiết bị theo thứ tự của biến đếm
		data = ([my_response["id"], my_response["hostname"], my_response["managementIpAddress"], my_response["series"], my_response["reachabilityStatus"]])
		my_table.append(data)  # append dùng để thêm vào dữ liệu trả về vào list my_table đã được tạo ở trên, tương đương với thêm 1 dòng mới
		i += 1  

	table = tabulate(my_table, headers='firstrow', tablefmt='psql')   # header là để chọn hàng đầu tiên làm header cho bảng
																	  # tablefmt là để tạo format cho bảng, còn nhiều format khác nữa  
	print(table)


theTicket=getTicket()
getNetworkDevices(theTicket)