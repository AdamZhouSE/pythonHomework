times = []
b = []
n = 0
tmax = 0
def f(m : int) -> bool:
    global times, tmax, n
    b = [-1 for i in range(m)]
    for i in range(m):
        b[i] = times[i] # 第一批奶牛
    b = sorted(b)
    for i in range(m, n):
        if b[m-1] > tmax: return False
        b[0] += times[i]
        b = sorted(b)
    return b[m-1] <= tmax

if __name__ == '__main__':
    x = input().strip().split()
    n = int(x[0])
    tmax = int(x[1])
    l = 1
    r = n
    for i in range(n):
        times.append(int(input()))
        b.append(0)

    while l <= r:
        m = (l+r)//2
        if f(m): r = m-1
        else: l = m+1

    print(l)
