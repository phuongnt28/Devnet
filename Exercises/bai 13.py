import datetime

### from datetime import * là import tất cả module, khi đó chỉ cần gõ datetime.now()
### còn import datetime thôi. thì khi gõ phải datetime.datetime.now()


ten=input("Nhap ten:")
tuoi=int(input("Nhap tuoi:"))

nam=datetime.datetime.now().year-tuoi+100
print("Đến năm %d bạn %s sẽ 100 tuổi" %(nam,ten))
