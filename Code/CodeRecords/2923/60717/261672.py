tmp=input().split()
n=int(tmp[0])
q=int(tmp[1])
list1=input().split()
for i in range(0,n):
    list1[i]=int(list1[i])
list2=[0 for i in range(0,n)]
for i in range(0,q):
    tmp=input().split()
    l=int(tmp[0])
    r=int(tmp[1])
    for j in range(l-1,r):
        list2[j]+=1
summ=0
while len(list1)!=0
    summ+=(max(list1)*max(list2))
    list1.remove(max(list1))
    list2.remove(max(list2))
print(summ)