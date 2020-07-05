n = int(input())
l=input().split()
print(len(l),n)
l.sort()
print(len(l))
s=""
for i in range(n):
    s=l[i]+s
print(int(s),end="")