n = int(input())
l=input().split()
print(len(l),n)
l.sort()
s=""
for i in range(n):
    s=l[i]+s
print(int(s),end="")