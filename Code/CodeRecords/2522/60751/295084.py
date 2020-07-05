arr2=list(map(int,input().strip("[").strip("]").split(",")))
arr1=list(map(int,input().strip("[").strip("]").split(",")))
num=[]
for i in arr1:
    j=0
    while(j<len(arr2)):
        if arr2[j]==i:
            num.append(i)
            del arr2[j]
            j-=1
        j+=1
num.extend(sorted(arr2))
print(num)