n=int(input("Enter your number:"))
print ("Picture 1:")
#Print on per line
for row in range(n):     
    for column in range(n):
        if row+column <= n-1:
            print("* ", end="")
        else:
            print(" ", end="")
    #Xuống dòng
    print()