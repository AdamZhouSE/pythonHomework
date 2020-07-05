"""
A是否可以写成B个不同的正整数之和
k个不同的正整数相加最小为1+2+3+4+...+k
即 k(k-1)/2
所以只要A >= k(k+1)/2, 就可以
"""
t = int(input())
for i in range(t):
    inp = input().split(" ")
    a, b = int(inp[0]), int(inp[1])
    require = b*(b+1)//2
    if a >= require:
        print(1)
    else:
        print(0)
