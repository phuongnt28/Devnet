#List
Lst=[3,5,9,-5,2,4,8]
print(Lst)
print("Tong=", sum(Lst))

S='3,5,9,-5,2,4,8'
Lst=list(map(int,S.split(",")))
print("list 2:",*Lst)
print("Tong 2=", sum(Lst))
print("So nho nhat la:", min(Lst))


#Câu 3
#a,b
lst = [1, -1, 2, 0, 5, 8, -13, 21, -34, 55, 87, 0]
for i in lst:
    if i < 5:
        print(i, end=" ")
print()
#c
lst = [1, -1, 2, 0, 5, 8, -13, 21, -34, 55, 87, 0]
print("Cau c: Tao list chua cac so nho hon 5 co trong lst1", end=":")
lst2=[]
for i in lst:
    if i<5:
        lst2.append(i)
print(' lst2=',lst2)
        