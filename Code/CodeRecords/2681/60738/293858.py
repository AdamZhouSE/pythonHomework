n=int(input())
for i in range(n):
    N=int(input())
    time=0
    while(N!=0):
        if(N%2==0):
            N=int(N/2)
            time+=1
        elif (N%2==1):
            N-=1
            time+=1
    print(time)