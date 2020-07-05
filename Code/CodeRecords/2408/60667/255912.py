import math
n = int(input())
if n<=2:
    print(1)
    quit()
count = 0
for i in range(2, n+1):
    for j in range(2,i):
        if i % j == 0:
            count = count - 1
            break
    count += 1
print(math.factorial(count)*math.factorial(n-count) % 1000000007)  