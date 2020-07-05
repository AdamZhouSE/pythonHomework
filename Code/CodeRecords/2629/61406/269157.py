T = int(input())
for x in range(0,T):
    n = int(input())
    a = bin(n)[2:]
    count = a.count('1')
    print(count)