n = int(input())
l = input().split()
for i in range(n):
    l[i] = int(l[i])
l.sort()
for i in range(n-1):
    print (l[i],end=" ")
print (l[n-1])