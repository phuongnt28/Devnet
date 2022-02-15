n=int(input("Nhập số nguyên dương:"))
S=0
for so in range(1,n+1):     #n=5 => range(1,n+1)
    S+=(1/so)
print("Tổng các số từ 1 đến %d là %.4f" %(n,S)) #%.xf với x là số số lẻ cần lấy (default là 6)