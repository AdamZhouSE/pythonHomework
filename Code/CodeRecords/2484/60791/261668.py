from collections import Counter
def solve(a,b):
    seen = set()
    for item in a:
        if item not in seen:
            seen.add(item)
    for item in b:
        if item not in seen:
            seen.add(item)            
    return len(seen)


T = int(input())
x = 0
while(x<T):
    x+=1
    N = int(input())
    a = [int(i) for i in input().split(' ')]
    b = [int(i) for i in input().split(' ')]
    print(solve(a,b))