n=int(input())
start=int(input())
print([start^i^(i >> 1) for i in range(1 << n)])