def solve(n):
    res = False
    n
    for i in range(n):
        if n-i%i==0 :
            res = True
            n = n-i
    if(True):
        return 1+solve(n)
    else:
        return 0


T = int(input())
x = 0
while(x<T):
    x+=1
    print(solve(int(input()))%2)
    