def K_subArr():
    T=int(input())
    for i in range(0,T):
        row1=input().split(" ")
        N=int(row1[0])
        K=int(row1[1])
        arr=input().split(" ")
        arr=",".join(arr)
        arr=eval("["+arr+"]")
        res=0
        for i in range(0,N-K+1):
            sum=0
            for j in range(i,i+K):
                sum+=arr[j]
            res=max(sum,res)
        print(res)

if __name__=='__main__':
    K_subArr()