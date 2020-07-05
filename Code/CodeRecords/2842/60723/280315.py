n=int(input())
array=[0]*n
for i in range(n):
    temp=int(input())
    if temp==-1:
        array[i]=-1
    else:
        array[i]=temp-1
count=[]
for i in range(n):
    j=i
    temp=0
    while array[j]!=-1:
        temp=temp+1
        j=array[j]
    count.append(temp)
print(max(count)+1)