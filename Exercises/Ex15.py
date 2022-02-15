print("Câu A")
n=15
if n%2==0:
    print(n, "là số chẵn")
else:
    print(n, "là số lẻ")

print("Câu B")
if n%4==0:
    print (n, "chia chắn cho 4")
elif n%2==0:
    print (n, "chia chẵn cho 2")
else:
    print (n, "không chia hết cho 4 và 2")

print("Câu C")
n=int(input("Nhập số nguyên n:"))
m=int(input("Nhập số nguyên m:"))
if n%m==0:
    print("%d là bội số của %d" %(n,m))
else:
    print("%d KHÔNG là bội số của %d" %(n,m))

