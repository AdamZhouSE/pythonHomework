T = int(input())
for a in range(0,T):
    n = int(input())
    source = input().split(' ')
    result = 0
    for x in range(0,n):
        h = 10000
        for y in range(x,n):
            h = min(h,int(source[y]))
            result = max((y-x+1)*h,result)
    print(result)

