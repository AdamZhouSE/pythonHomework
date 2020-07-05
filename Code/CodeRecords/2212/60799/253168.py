T = int(input())
for ttt in range(T):
    n = int(input())
    res = 0
    for i in range(1,int(n*0.5)+1):
        if n%i ==0:
            res +=i
            if res>=n:
                break
    if res >= n:
        print(0)
    else:
        print(1)