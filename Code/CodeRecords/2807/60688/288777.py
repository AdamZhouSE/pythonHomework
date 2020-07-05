l1=0
l2=0
l3=0
l4=0
reqlist=input().split(" ")
numslist1=input().split(" ")
numslist2=input().split(" ")
n=int(reqlist[0])
m=int(reqlist[1])
list1=list(int(a) for a in numslist1)
list2=list(int(b) for b in numslist2)
for i in range(0,n):
    if(list1[i]%2==1):
        l1=l1+1
    else:
        l2=l2+1
for j in range(0,m):
    if(list2[j]%2==1):
        l3=l3+1
    else:
        l4=l4+1
res=min(l1,l4)+min(l2,l3)
print(res)