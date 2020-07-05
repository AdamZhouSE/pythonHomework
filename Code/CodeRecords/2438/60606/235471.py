array = input()
result = array[1:len(array)-1].split(",")
result.sort()
for i in range(0,len(result)):
    result[i] = int(result[i])
print(result)
