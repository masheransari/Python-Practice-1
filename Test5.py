print("BMI Calculator")

weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))

BMI = weight/(height**2)

print("BMI: "+str(BMI))