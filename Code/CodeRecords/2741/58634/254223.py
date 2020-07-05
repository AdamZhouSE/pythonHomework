array = eval(input())
maxLen = 0
l = 1
for i in range(0,len(array)-1):
    if(array[i]<array[i+1]):
        l+=1
    else:
        maxLen = max(l,maxLen)
        l = 1
print(maxLen)