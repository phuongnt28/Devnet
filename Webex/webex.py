import storage
import requests
import json

base_url = "https://webexapis.com/v1/"

def get_rooms():
    url = base_url + "rooms"
    headers = {
        "Content-Type" : "application/json",
        "Authorization": "Bearer " + storage.token
    }

    resp = requests.get(url, headers=headers)
    data = resp.json()
    print(json.dumps(data, indent=4))

def post_message(toPerson, text):
    url = base_url + "messages"

    headers = {
        "Content-Type": "application/json" ,
        "Authorization": "Bearer " + storage.token
    }
    body = {                    # là kiểu dữ liệu Dictionnary
        "toPersonEmail": toPerson,
        "text" : text
    }
    resp = requests.post(url, headers=headers,json=body)
    print(resp.json())  

def menu():
    print("""
        1. Lấy danh sách các phòng
        2. Gửi tin nhắn
        0. Thoát chương trình
    """)
    choice = int(input("Nhập lựa chọn: "))
    return choice

def main():
    while True:
        choice = menu()
        if choice == 1:
            get_rooms()
        if choice == 2:
            toPerson = input("Gửi đến: ")
            text = input("Tin nhắn: ")
            post_message(toPerson, text)
        if choice == 0:
            break

main()
# post_message()
# get_rooms()