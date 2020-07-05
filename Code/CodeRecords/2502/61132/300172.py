t = int(input())
l=[]
for j in range(t):
    l.append(int(input()))
l.sort()
print(sum(l[1:]))