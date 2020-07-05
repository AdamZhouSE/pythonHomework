tmp=input().split()
n=int(tmp[0])
k=int(tmp[1])
list1=input().split()
for i in range(0,n):
    list1[i]=int(list1[i])
list2=[]
for i in range(0,n-1):
    list2.append(list1[i+1]-list1[i])
list2.sort()
summ=0
for i in range(0,k):
    summ+=list2[n-2-i]
print(list1[n-1]-list1[0]-summ)