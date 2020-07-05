n=int(input())
lists=input().split()
for i in range(n):
    lists[i]=int(lists[i])
s=0
d=0
counter=1
while n>0:
    if counter%2==1:
        if lists[0]>lists[n-1]:
            s+=lists[0]
            lists.pop(0)
        else:
            s+=lists[n-1]
            lists.pop(n-1)
    else:
        if lists[0]>lists[n-1]:
            d+=lists[0]
            lists.pop(0)
        else:
            d+=lists[n-1]
            lists.pop(n-1)
    counter+=1   
    n-=1
print(s,end=" ")
print(d)