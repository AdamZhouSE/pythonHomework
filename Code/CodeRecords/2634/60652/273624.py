a=list(map(int,input().replace('[','').replace(']','').split(',')))
k=int(input())
arr=[]
for i in range(len(a)-1):
    for j in range(i,len(a)):
        arr.append([a[i]/a[j],[a[i],a[j]]])
arr.sort(key=lambda x:x[0])
print(arr[k-1][1])