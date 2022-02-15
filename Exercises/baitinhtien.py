sotien=int(input("Nhap so tien: "))
to500=sotien//500
sotien=sotien%500

to200=sotien//200
sotien=sotien%200

to100=sotien//100
sotien=sotien%100

to50=sotien//50
sotien=sotien%50

to20=sotien//20
sotien=sotien%20

to10=sotien//10
sotien=sotien%10

to5=sotien//5
sotien=sotien%5


to2=sotien//2  ##to100=0
sotien=sotien%2

to1=sotien

print("So to 500:",to500)
print("So to 200:",to200)
print("So to 100:",to100)
print("So to 50:",to50)
print("So to 20:",to20)
print("So to 10:",to10)
print("So to 5:",to5)
print("So to 2:",to2)
print("So to 1:",to1)