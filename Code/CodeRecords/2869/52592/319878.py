a=int(input())
b=input().split()
l=[]
for i in range(len(b)):
    l.append(int(b[i]))

l.reverse()
l2=[]
for i in l:
    if i not in l2:
        l2.append(i)
l2.reverse()
leg=len(l2)
print(leg)
for i in range(leg-1):
    print(l2[i],end=" ")
print(l2[leg-1])
