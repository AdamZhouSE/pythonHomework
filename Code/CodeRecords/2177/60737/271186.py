a = [0 for i in range(200)]
k = int(input())
n = k + 1
print(n)
a[n] = n
i = n - 2
while i>0:
    a[i] = a[i + 2] - 1
    i -= 2
a[n-1] = 1    
i = n - 3
while i>0:
    a[i] = a[i + 2] + 1
    i -= 2
for m in range (1, n+1):
    print(a[m], end=" ")
    