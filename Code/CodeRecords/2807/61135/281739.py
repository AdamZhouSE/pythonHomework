input1=input().split(" ")
input2=input().split(" ")
input3=input().split(" ")
n=int(input1[0])
m=int(input1[1])
list1=list(int(a) for a in input2)
list2=list(int(b) for b in input3)
l1=0
l2=0
l3=0
l4=0
for a in range(0,n):
    if(list1[a]%2==1):
        l1=l1+1
    else:
        l2=l2+1
for b in range(0,m):
    if(list2[b]%2==1):
        l3=l3+1
    else:
        l4=l4+1
res=min(l1,l4)+min(l2,l3)
print(res)
