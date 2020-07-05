n=int(input())
k=int(input())
nums=[]
for i in range(n):
    nums.append(i+1)
res=[]
i=0
while i<n:
    tem=1
    for j in range(1,n-i):
        tem*=j
    if k/tem!=int(k/tem):
        res.append(nums.pop(int(k/tem)))
        k=k%tem
    else:
        res.append(nums.pop(int(k/tem)-1))
        k=tem
    i+=1
print(''.join(str(i) for i in res))