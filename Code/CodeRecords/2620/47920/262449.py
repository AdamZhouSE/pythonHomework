import math

t = int(input())
def f(n):
    su =0
    res = 0
    if(n == 1):
        res = 1
    else:
        for i in range(n):
            su = su + math.pow(n,3)
    return res

for i in range(t):
    
    inp = int(input())
    result = 0
    for i in range(inp+1):
        result = result + math.pow(i,5)
    print(int(result))