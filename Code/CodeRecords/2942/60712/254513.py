n = int(input())
l=input().split()
l.sort()
s=""
for i in range(len(l)):
    s=l[i]+s
print(int(s),end="")