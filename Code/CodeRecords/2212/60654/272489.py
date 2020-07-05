a = int(input())
for i in range(a):
    b = int(input())
    sum = b
    for j in range(1,b):
        if b%j == 0:
            sum -= j
    if sum>0:
        sum = 1
    else:
        sum = 0
    print(sum)    