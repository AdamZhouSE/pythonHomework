a=input()
arr = a.split(",")
dif = int(input())
maxLen = 0
i=0
while i<len(arr)-1:
    res = 0
    j=i+1
    temp = i
    while i<len(arr)-1 and int(arr[j])-int(arr[i])==dif:
        i=j
        j+=1
        res+=1
    i=temp+1
    if res>maxLen:
        maxlen = res
print(maxLen)