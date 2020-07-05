def handshakes(n):
    if n%2==1:
        return handshakes(n-1)
    if n == 0:
        return 1
    res = 0
    for i in range(0, n, 2):
        res += handshakes(i) * handshakes(n - 2 - i)
    return res

t = int(input())
for i in range(t):
    n=int(input())
    print(handshakes(n))