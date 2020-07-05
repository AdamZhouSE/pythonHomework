def re(n):
    if(n==1):
        return 1
    else:
        result = int(re(n-1)*(4(n-1)-2)/(n-1))
        return result
n = int(input())
if(n==1):
    print(1)
else:
    result = 1
    now = 2
    while(now <= n):
        result = int(result*(4*(now-1)-2)/(now-1))
        now+=1
    print(result)
