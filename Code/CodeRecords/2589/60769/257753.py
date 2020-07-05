def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        pre = 1
        prepre = 2
        while n > 1:
            temp = pre
            pre = pre + prepre
            prepre = temp
            n -= 1
        return pre


num = int(input())
for j in range(num):
    nn = int(input())
    print(lucas(nn)%1000000007)