T = int(input())
a = []
b = []
for i in range(T):
    inp = input().split()
    a.append(int(inp[0]))
    b.append(int(inp[1]))
for i in range(T):
    n=a[i]
    k=b[i]
    print(k**(n-1))