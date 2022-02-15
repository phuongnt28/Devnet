n=int(input("Enter n: "))
Total=0
number=1
while number<n:
    if number%2==0:
        Total+=number
    number+=1
print("Sum of the even numbers from 1 to %d is %d" %(n,Total))