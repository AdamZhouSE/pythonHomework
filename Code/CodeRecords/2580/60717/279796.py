m=int(input())
n=int(input())
ops=int(input())
list1=[[0for i in range(0,n)]for i in range(0,m)]
listx=[]
listy=[]
for i in range(0,ops):
    tmp=input().split(',')
    a=int(tmp[0])
    b=int(tmp[1])
    listx.append(a)
    listy.append(b)
count=0
for i in list1:
    for j in i:
        if j==list1[0][0]:
            count+=1
print(min(listx)*min(listy))
        