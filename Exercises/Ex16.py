sotien=int(input("Nhap so tien: "))

soto500=sotien//500
if soto500>0:
        print("Có %d tờ 500"  %soto500)
sotien=sotien%500

soto200=sotien//200
if soto200>0:
    print("Có %d tờ 200"  %soto200)
sotien=sotien%200

soto100=sotien//100
if soto100>0:
    print("Có %d tờ 100"  %soto100)
sotien=sotien%100

soto50=sotien//50
if soto50>0:
    print("Có %d tờ 50"  %soto50)
sotien=sotien%50

soto20=sotien//20
if soto20>0:
    print("Có %d tờ 20"  %soto20)
sotien=sotien%20

soto10=sotien//10
if soto10>0:
    print("Có %d tờ 10"  %soto10)
sotien=sotien%10

soto5=sotien//5
if soto5>0:
    print("Có %d tờ 5"  %soto5)
sotien=sotien%5


soto2=sotien//2  ##to100=0
if soto2>0:
    print("Có %d tờ 2"  %soto2)
sotien=sotien%2

soto1=sotien
Tongsoto=soto500+soto200+soto100+soto50+soto20+soto10+soto5+soto2+soto1
print("Tổng số tờ là %d" %Tongsoto)