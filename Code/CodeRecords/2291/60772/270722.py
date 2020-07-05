def haff(a,b,n):
    for i in range(0,2):
        for j in range(0,n-1):
            if a[j] < a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
    b[0] = a[n-1]
    b[1] = a[n-2]
    a[n-2] = b[0] + b[1]
    a[n-1] = float('inf')
    return a[n-2]

a = []
b = [0,0]
sum = 0
n = int(input())
for i in range(1000):
    a.append(float('inf'))
li = input().split()
for i in range(n):
    a[i] = int(li[i])
k = 0
while a[1] != float('inf'):
    sum += haff(a,b,n-k)
    k += 1
print(sum)