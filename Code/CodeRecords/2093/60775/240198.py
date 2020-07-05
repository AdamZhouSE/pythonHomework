n = int(input())
k = int(input())
l = list(range(1,n+1))
result = ''

def factorial(x):
    result = x
    for i in range(1,x):
        result *= i
    return result

while len(result) < n-1:
    tmp = (k-1)//factorial(len(l)-1)
    result = result + str(l[tmp])
    k = k - tmp * factorial(len(l)-1)
    del l[tmp]
result = result + str(l[tmp])

print(result)