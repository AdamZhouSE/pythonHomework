import math
def solve(x) : 
    if (x < 10): 
        return x
    res = x/10 + 9
    first=x
    while (first >= 10) : 
        first = first/10
    last = x % 10
    if (first>last) : 
        res = res - 1
    return res 

t=int(input())
for nn in range(t):
    a,b=input().split()
    a,b=int(a),int(b)+1
    print(solve(b) - solve(a - 1))

    