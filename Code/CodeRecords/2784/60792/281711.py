n,m=map(int,input().split(" "))
count=[]
pos=0
for i in range(0,n):
    count.append(0)
for i in range(0,m):
    list1=list(map(int,input().split(" ")))
    max=0
    for j in range(0,n):
        if list1[j]>max:
            max=list1[j]
            pos=j
    count[pos]+=1
max=0
for i in range(0,n):
    if count[i]>max:
        max=count[i]
        pos=i
print(pos+1)