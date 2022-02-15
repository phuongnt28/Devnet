n=int(input("Nhập số nguyên dương:"))
S=0
for so in range(2,n+1):     #n=5 => range(1,n+1)
    S+=(1/so)
print("Tổng S từ 2 đến %d là %.4f" %(n,S)) #%.xf với x là số số lẻ cần lấy (default là 6)