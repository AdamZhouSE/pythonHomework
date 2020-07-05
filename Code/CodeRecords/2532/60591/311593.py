arr = eval(input().strip())
maxStack = [arr[0]]
for x in range(1,len(arr)):
    if(arr[x] < maxStack[-1]):
        continue
    elif(arr[x] == maxStack[-1]):
        maxStack.append(arr[x])
    else:
        j = len(maxStack) - 1
        tempMax = arr[x]
        while(j >= 0 and maxStack[j] > arr[x]):
            if(maxStack[j] > tempMax):
                tempMax = maxStack[j]
            del maxStack[j]
            j -= 1
        maxStack.append(tempMax)
print(len(maxStack))
