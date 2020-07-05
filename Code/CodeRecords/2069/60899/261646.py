a = list(input())
b = list(input())
a = list(map(int,a))
b = list(map(int,b))
m = 0
n = 0
for i in range(len(a)):
    m = m*10+a[i]
for i in range(len(b)):
    n = n*10+b[i]
print(m*n)