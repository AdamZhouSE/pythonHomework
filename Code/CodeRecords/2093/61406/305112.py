def factorial(x):
    result = 1
    for i in range(1, x + 1):
        result = result * i
    return result


n = int(input())
k = int(input())
result = ""
statistics = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
while k != 0:
    if k%factorial(n-1)==0:
        num = k//factorial(n-1)
    else:
        num = k // factorial(n - 1) + 1
    while statistics[num] == 0:
        num = num + 1
    result = result + str(num)
    statistics[num] = 0
    k = k % factorial(n - 1)
    n = n - 1
for i in range(1,10):
    if statistics[i]==1:
        result = result+str(i)
        break
print(result)


