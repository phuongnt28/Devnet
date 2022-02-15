Score=int(input("Enter your score: "))
if 0<=Score<65:
    print("Your classification is E")
elif 65<=Score<=69:
    print("Your classification is D")
elif 69<Score<=79:
    print("Your classification is C")
elif 79<Score<=80:
    print("Your classification is B")
elif 89<Score<=100:
    print("Your classification is A")
else:
    print("Error")