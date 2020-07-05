n = int(input())
l = input().split()
for i in range(n):
    l[i] = int(l[i])
l.sort()
if l[-1]-l[1] > l[-2]-l[0]:
    res = l[-2]-l[0]
else:
    res = l[-1]-l[1]
print (res)