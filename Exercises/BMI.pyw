name=input("Enter your name: ")
height_m=float(input("Enter height in metter: "))
weight_kg=float(input("Enter your weight in kilogram: "))
bmi=weight_kg / (height_m**2)
if 0<=bmi<18.5:
    print(name, end=" ")
    print("is underweight with bmi %d" %bmi)
elif 18.5<=bmi<25:
    print(name, end=" ")
    print("is normal with bmi %d" %bmi)
elif 25<=bmi<30:
    print(name, end=" ")
    print("is overweight with bmi %d" %bmi)
elif 30<=bmi<35:
    print(name, end=" ")
    print("is obese with bmi %d" %bmi)
else:
    print(name, end=" ")
    print("is extremly obese with bmi %d" %bmi)