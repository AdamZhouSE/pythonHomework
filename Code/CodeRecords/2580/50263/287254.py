m = int(input())
n = int(input())
num = int(input())
x = n
y = m
for i in range(num):
    p,q = input().split(',')
    x = min(x, int(p))
    y = min(y, int(q))
res = x*y
print(res)