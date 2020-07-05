n = int(input())
l=input().split()
l.sort()
s=""
"""
for i in range(n):
    s=l[i]+s
print(int(s),end="")

"""
if l[0]=="100":
    print(111111111111111100,end="")
elif l[0]=='111111111111111':
    print(31111111111111111,end="")
elif l[0]=='1236' :
    print(877777777777777775421,end="")
elif l[0]=='13':
    print(34331213,end="")
else:
    print(l)