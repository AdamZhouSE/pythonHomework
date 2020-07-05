arr=[int(n) for n in input().split(' ')]
n,k=arr[0],arr[1]
list=[]
for i in range(0,k):
    at=[int(n) for n in input().split(' ') ]
    list.append(at)
num=0
index=[]
for i in range(0,k):
    index.append(0)
for i in range(0,n):
    a=list[0][i]
    mark=0
    for j in range(1,k):
        ino=0
        for m in range(index[j],n):
            if list[j][m]==a:
                ino=1
                index[j]=m+1
                break
        if ino==1:
            continue
        else:
           mark=1
           break
    if mark==0:
        num=num+1
print(num)