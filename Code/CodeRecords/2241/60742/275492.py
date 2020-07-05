n = int(input())
res = 1
while n%2==0:
    n = n//2
if n>2:
    res += 1
for i in range(2,n):
    if n%i==0:
        if (2*i+1)*i>n:
            res += 1
print(res)