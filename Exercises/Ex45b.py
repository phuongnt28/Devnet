n=int(input("Nhap số nguyên dương:"))
S=0
for so in range(0,n+1):     #n=5 => range(1,n+1)
    S+=2*so +1
print("Tổng các số từ 1 đến %d là %d" %(n,S))