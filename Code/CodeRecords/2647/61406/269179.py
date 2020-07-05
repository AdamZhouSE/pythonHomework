T = int(input())
for a in range(0,T):
    N = int(input())
    x = bin(N)[2:]
    print(x.count('1'))