m = int(input())
for v in range(0, m):
    I, L = map(int, input().split())
    #num = int(input())
    s = ""
    for i in range(0, L):
        s += '1'
    n = int(s, 2)
    print(n-I+1)