arr = eval(input().strip())
maxStack = [arr[0]]
for x in range(1,len(arr)):
    if(arr[x] < maxStack[-1]):
        j = len(maxStack) - 1
        temp_max = 0
        while(j >= 0 and maxStack[j] > arr[x]):
            if(temp_max < maxStack[j]):
                temp_max = maxStack[j]
            del maxStack[j]
            j-=1
        maxStack.append(temp_max)
    elif(arr[x] >= maxStack[-1]):
        maxStack.append(arr[x])
print(len(maxStack))
