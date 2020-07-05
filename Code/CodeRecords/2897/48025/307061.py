arr=eval(input())
max=0
def isQualified(word1,word2):
    for c in word1:
        if c in word2:
            return False
    return True

for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if(isQualified(arr[i],arr[j])):
            if(max<len(arr[i])*len(arr[j])):
                max=len(arr[i]*len(arr[j]))
print(max)