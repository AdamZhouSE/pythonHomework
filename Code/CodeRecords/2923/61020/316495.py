#python 3.5.2

n,q = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
arr.sort()
occ = [0] * n

for i in range(q):
    l, r = map(int, input().split())
    occ[l-1]+=1
    if (r < n): occ[r]-=1
    
for i in range(1,n):
    occ[i]+=occ[i-1]
occ.sort()    
    
sum = 0
for i in range(n):
    sum += arr[i] * occ[i]

print (sum)
