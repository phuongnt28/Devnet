n=int(input("Enter n: "))
evenTotal=0
number=1
while number<n:
    if number%2==0 and n%number==0:
        evenTotal+=number
    number+=1
print("Sum of the even numbers from 1 to %d is %d" %(n,evenTotal))