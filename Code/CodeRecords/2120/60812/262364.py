n = int(input())
m = 1
for i in range(2, n):
    temp1, temp2 = n//i, n % i
    num, count = 1, 0
    for j in range(i):
        if count < temp2:
            num *= temp1+1
            count += 1
        else:
            num *= temp1
    if num > m:
        m = num
    else:
        break
print(m)