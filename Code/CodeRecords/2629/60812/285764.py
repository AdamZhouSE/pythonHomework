T = int(input())
for i in range(T):
    N = int(input())
    print(bin(N).replace('0b', '').count('1'))