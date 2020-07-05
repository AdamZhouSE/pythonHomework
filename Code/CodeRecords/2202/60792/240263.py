def cal(n):
    result=1
    for i in range(1,n+1):
        result=result*i
    return result

num=int(input())
for i in range(0,num):
    n=int(input())
    rem=n//2
    count=0
    for i in range(0,rem+1):
        count=count+cal(i+n-2*i)/(cal(i)*cal(n-2*i))
    print(int(count))
    