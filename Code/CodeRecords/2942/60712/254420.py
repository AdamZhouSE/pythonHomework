n = int(input())
l=input().split()

l.sort()
s=""
for i in range(n-1,-1,-1):
    s=s+l[i]
print(int(s),end="")

