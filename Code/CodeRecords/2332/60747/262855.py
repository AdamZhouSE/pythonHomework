import math
x=int(input())
target=int(input())
n = int(math.log(target,x))
mask = x**n
last = [0,n+1]
for i in range(n,-1,-1):
    d = target//mask
    multis = 2 if i==0 else i
    last = [min(last[1]+(x-d)*multis,last[0]+d*multis), min(last[1]+(x-d-1)*multis,last[0]+(d+1)*multis)]
    target = target % mask
    mask /=x
print(int(last[0])-1)