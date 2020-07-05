t=int(input())
while(t):
        n=int(input())
        if(1<=n<=pow(10,7)):
            arr=list(map(int,input().split()))
            if(n==len(arr)):
                for i in range(n-1):
                    if(arr[i]>arr[i+1]):
                        print(arr[i+1],end=' ')
                    else:
                        print('-1',end=' ')
                print('-1 ')
        t=t-1
