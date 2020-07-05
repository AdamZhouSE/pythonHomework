n = int(input())
l=input().split()
l.sort()
s=""
for i in range(len(l)-1):
    s=l[i]+s
print(int(s),end="")

