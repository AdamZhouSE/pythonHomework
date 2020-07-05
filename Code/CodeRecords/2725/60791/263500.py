def solve(n):
    res = False
    for i in range(1,n):
        if (n-(n-i))%(n-i)==0 :
            res = True
            n = i
    if(res):
        return 1+solve(n)
    else:
        return 0


T = int(input())
x = 0
arr = []
temp = []
while(x<T):
    x+=1
    a = int(input())
    temp.append(a)
    res = solve(a)%2
    arr.append(res)
    print(res)