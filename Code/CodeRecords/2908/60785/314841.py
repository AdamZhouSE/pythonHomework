n=int(input())
l=[]
for ff in range(n):
    l.append(input().split())
for i in l:
    i.sort()
print(l)
