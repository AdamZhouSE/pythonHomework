def cal(i):
    ds = []
    if i == 1:
        return 0
    else:
        x = 2
        while x < i + 1:
            if i % x == 0:
                ds.append(x)
                i /= x
                x -= 1
            x += 1
        return ds

t = int(input())
for x in range(t):
    print(cal(int(input())))
