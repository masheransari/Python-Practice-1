import cmath

# Determinant D of a quadratic equation is defined as b 4ac 2  . Write a program in python
# that takes three inputs a, b, and c from the user. Then calculate Determinant D and print
# it. Then find the real roots according to following three cases.


print("DSTT Fall 2021\nLab 1 Task\nQuadratic Equation Solution-----------")
a = float(input("Enter A: "))
b = float(input("Enter B: "))
c = float(input("Enter C: "))

underRootCalc = (b * b) - (4 * a * c)

if underRootCalc > 0:
    plusResult = (-(b) + cmath.sqrt(underRootCalc)) / (2 * a)
    negativeResult = (-(b) - cmath.sqrt(underRootCalc)) / (2 * a)
    print("Positive Condition")
    print("2 Real Root Are: " + str(plusResult)+ " and " + str(negativeResult))

elif underRootCalc == 0:
    print("O Conidtion")
    singleRoot = (-b) / (2 * a)
    print("1 Real root we have " + str(singleRoot))
else:
    print("Less than 0 condition")
    print("Only Complex Root!")
