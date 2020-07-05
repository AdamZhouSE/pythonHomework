m=int(input())
n=int(input())
ops=int(input())
list1=[[0for i in range(0,n)]for i in range(0,m)]
for i in range(0,ops):
    tmp=input().split(',')
    a=int(tmp[0])
    b=int(tmp[1])
    a=min(a,m-1)
    b=min(b,n-1)
    for j in range(0,a):
        for k in range(0,b):
            list1[j][k]+=1
count=0
for i in list1:
    for j in i:
        if j==list1[0][0]:
            count+=1
print(count)
        