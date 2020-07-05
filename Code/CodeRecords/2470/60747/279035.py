n=int(input())
result=[]
for i in range(n):
    size=int(input())
    num=input().split(" ")
    arr=[]
    new=[]
    k=0
    s=""
    for j in range(size*size):
        arr.append(num[j])
        if len(arr)%size==0:
            new.append(arr)
            arr=[]
    for k in range(size):
        p=size-1
        while p>=0:
            s=s+str(new[p][k])+" "
            p-=1
    result.append(s)
for f in range(n):
    print(result[f])