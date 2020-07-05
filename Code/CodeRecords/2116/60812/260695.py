n = int(input())
l = [int(i) for i in input().split(',')]
count = 1
num = 2
while count < n:
    temp = num
    for j in l:
        while temp % j == 0:
            temp //= j
    if temp == 1:
        count += 1
    num += 1
print(num-1)