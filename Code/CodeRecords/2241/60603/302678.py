def sums(N):
    a=[]
    count=0
    for i in range(1,N+1):
        if i%2==0:
            if (N/i+0.5)%1==0:
                #a=[i for i in range((N/i+0.5-i/2),(N/i+0.5+i/2))]
                if N/i+0.5-i/2>=1:
                    count=count+1
                else:
                    break
        else:
            if (N/i)%1==0:
                if N/i-(i-1)/2>=1:
                    count=count+1
                else:
                    break
    print(count)
N=int(input())
sums(N)