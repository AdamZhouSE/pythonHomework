l0 = input().split()
n = int(l0[0])
m = int(l0[1])
l = [0]*m
for i in range(n):
    l1 = input().split()
    k = int(l1[0])
    for j in range(1,k+1):
        l1[j] = int(l1[j])
    for j in range(1,k+1):
        if l[l1[j]-1]==0:
            l[l1[j]-1]=1
if 0 in l:
    print ("NO")
else:
    print ("YES")