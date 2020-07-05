t= int(input())
for i in range(t):
    inp = input().split(" ")
    n = int(inp[0])  #给定的n天
    k = int(inp[1])  #
    re = 1
    for i in range(n-1):
        re = re * k
    print(re)