def solve(n):
    res = False
    for i in range(1,n):
        if n-i%i==0 :
            res = True
            n = n-i
    if(res):
        return 1+solve(n)
    else:
        return 1


T = int(input())
x = 0
while(x<T):
    x+=1
    print(solve(int(input()))%2)
    