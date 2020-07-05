t=int(input())
for i in range(0,t):
    n=int(input())
    result=0;
    for j in range(1,n+1):
        result+=j**5;
    print(result)