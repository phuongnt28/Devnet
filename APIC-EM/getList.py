import requests #Gửi các loại yêu cầu http đến server và nhận response
import json #Là định dạng dữ liệu để truyền và nhận dữ liệu với server
import sys # Để tương tác với hệ thống
from tabulate import tabulate #cung cấp các format bảng
import getTicket #Lấy các phương thức như get_auth_token, get trong file getTicket.py đã viết ở bài lab trước

device =[]
try:
    resp = getTicket.get(api="network-device") [I]# Lấy thông tin về network-device[/I]
    status = resp.status_code [I]#Lấy trạng thái của yêu cầu trên[/I]
    response_json = resp.json() [I]#Lấy nội dung json đã mã hóa từ lời đáp lại[/I]
    device = response_json["response"] [I]#Gán thông tin từ lời đáp lại vào device[/I]
except:                                                                                     
    print("Something wrong,cannot get network device info")
    sys.exit()

[I]# Nếu status khác 200(nghĩa là không thành công) thì in lời đáp lại và thoát chương trình[/I]
if status !=200:
    print (resp.text)
    sys.exit()

[I]# Nếu chuỗi trống thi in ra không có thiết bị được tìm thấy và thoát chương trình[/I]
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