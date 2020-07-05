t=eval(input())
for i in range(0,t):
    n=eval(input())
    result=0
    while(pow(2,result)<n):
        result+=1
    print(pow(2,result))