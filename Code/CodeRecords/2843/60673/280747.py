inp = int(input())
a = input().split(" ")
for i in range(inp):
    a[i]=int(a[i])
b = []
for i in range(inp-1):
    b.append( a[i] + a[i+1])
b.append(a[inp - 1])
for i in range(inp - 1):
    print (b[i], end="")
    print(" ", end="")
print(b[inp - 1])
