n = int(input())

if n < 3:
    print(0)
else:
    res = [1] * n
    res[0], res[1] = 0, 1
    for i in range(2, int(n ** 0.5) + 1):
        if res[i] == 1:
            res[i*2:n:i] = [0]*len(res[i*2:n:i])
    print(sum(res)-1)

