def cal(m,n,a,b):
    count = 0
    for x in range(m,n+1):
        if(x % a == 0 or x % b == 0):
            count += 1
    return count

n = eval(input())
while(n != 0):
    n = n - 1
    m,n,a,b = list(map(int,input().split(" ")))
    print(cal(m,n,a,b))