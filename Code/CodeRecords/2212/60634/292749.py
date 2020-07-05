#main-----
test = int(input())
for t in range(test):
    n = int(input())
    count = 0
    i = 1
    while i <= n:
        if n % i == 0:
            count += i
        i += 1
    if count < 2 * n:
        print(1)
    else:
        print(0)






































