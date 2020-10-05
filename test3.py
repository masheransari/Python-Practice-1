data = [12,24,35,24,88,120,155,88,120,155]

duplicateArray = set(data)
print(duplicateArray)
print("Sort Array as per Data Array")
resultArr = sorted(duplicateArray,key=data.index)
print(resultArr)
