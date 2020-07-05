num=input();
for i in range(num):
    N=input();
    result=0;
    for j in range(N+1):
        result=result+pow(N-j,2);
    print(result);