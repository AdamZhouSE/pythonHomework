read = lambda: eval(input())
read_line = lambda: [int(x) for x in input().split()]
n = read()
b = eval(input())
ugly: [int] = [1]
p = [0] * len(b)
# b = [2, 3, 5]
while n > 1:
    m = 1e18
    for x in range(len(b)):
        while True:
            v = ugly[p[x]] * b[x]
            if v > ugly[-1]:
                m = min(m, v)
                break
            p[x] += 1
    ugly.append(m)
    n -= 1
print(ugly[-1])
