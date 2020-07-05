def isQualified(result,item):
    if len(result) == 0:
        return True
    else:
        for i in range(len(result)):
            if item%result[i]!=0:
                return False
        return True


array = input().split(",")
array = [int(x) for x in array]
temp = []
max_length= 0
result = []
for i in range(len(array)):
    temp = []
    for j in range(i,len(array)):
        if isQualified(temp,array[j]):
            temp.append(array[j])
    if len(temp) > max_length:
        max_length = len(temp)
        result = temp.copy()
print(result)
