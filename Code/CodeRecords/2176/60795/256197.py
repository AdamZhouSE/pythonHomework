arr=list(input())
re=[]
for i in range(0,len(arr)):
    re.append(i)
prepos,lapos=-1,-1
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]>=arr[j]:
             arr[i],arr[j]=arr[j],arr[i]
             re[i],re[j]=re[j],re[i]
for i in range(0,len(arr)-1):
    print(re[i]+1,end=" ")
print(re[len(arr)-1]+1)
