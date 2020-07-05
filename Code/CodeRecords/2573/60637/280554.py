tests=(int)(input())
for i in range(tests):
    n=(int)(input())
    if(n%2==0):
        steps=(int)(n/2-1)
        result=2
        for j in range(steps):
            result=pow(result,3)
    else:
        steps=(int)((n-1)/2)
        result = 2
        for j in range(steps):
            result=pow(result,2)
    print(result)