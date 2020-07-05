a=eval(input())
for i in range(a):
    n=eval(input())
    start=1
    result=0
    while(n>0):
        result+=start*n
        n-=1
        start+=2
    print(result)