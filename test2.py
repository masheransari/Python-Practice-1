def smaller(intArray, arraySize, limit):
    count = 0
    validConditionStr =""
    for intNumber in intArray:
        if intNumber < limit:
            count+=1
            validConditionStr +=str(intNumber) + "<"+str(limit)+", "
    return str(count) + " ("+validConditionStr[:-2]+")"

x = {13, 56, 21, 45, 20, 43, 12, 43, 6}
print(smaller(x, len(x),21))
print(smaller(x, len(x),20))


