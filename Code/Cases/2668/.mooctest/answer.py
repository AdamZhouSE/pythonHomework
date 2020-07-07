
for t in range(int(input())):
    n = int(input())
    b = bin(n)
    x = (1 << (len(bin(n))-2))-1
    print(x-n, x)