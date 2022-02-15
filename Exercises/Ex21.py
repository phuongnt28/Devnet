a,b= map(int,input("Nhap vao 2 so:").split())
if a==0 and b ==0:
    print("Phương trình vô số nghiệm")
elif a==0 and b!=0:
    print("Phương trình vô nghiệm")
else:
    print("Nghiệm =", -b/a)