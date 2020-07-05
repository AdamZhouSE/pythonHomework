arr=list(map(int,input().replace('[','').replace(']','').split(',')))
n=len(arr)
a=[]
for i in range(n-1):
    count=0
    for j in range(i+1,n):
        if arr[i]>arr[j]:
            count+=1
    a.append(count)
a.append(0)
print(a)