l1 = input().split()
l2 = input().split()
n = int(l1[0])
x = int(l1[1])
l = [None]*n
res = 0
for i in range(n):
    l[i] = int(l2[i])
l.sort()
for num in l:
    res += num*x
    if x>1:
        x = x-1
print (res)