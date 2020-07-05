t = int(input())
for i in range(t):
    n = bin(int(input()))[2:]
    if n.count('1') == 1:
        print(len(n)-n.index('1'))
    else:
        print(-1)
