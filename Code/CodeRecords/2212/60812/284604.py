T = int(input())
for i in range(T):
    n = int(input())
    sum, i = 1, 2
    while i*i <= n:
        if n % i == 0:
            sum += i
            if i*i != n:
                sum += n//i
        i += 1
    if sum < n:
        print(1)
    else:
        print(0)