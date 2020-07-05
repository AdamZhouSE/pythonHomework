num=int(input())
l=input().split(" ")
for i in range(len(l)):
    l[i]=int(l[i])
#print(l)
for i in range(len(l)-1):
    minIndex=l.index(min(l[i:]))
    print(minIndex+1,end=" ")
    l1=l[i:minIndex]
    l1.reverse()
    l2=l[minIndex:minIndex+1]
    l=l[:i]+l2+l1+l[minIndex+1:]
    #print(l)
print(len(l),end=" ")