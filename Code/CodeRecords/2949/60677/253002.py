answer=input().split()
list=[]
list1=[]
n=list.__len__()
for i in answer:
    list.append(i)
n=list.__len__()
for i in range(2,n+1):
    list1.append(list[n-i])
print(" ".join(list1),end=" ")