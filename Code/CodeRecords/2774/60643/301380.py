def  solution(toys,k):
    toys=sorted(toys)
    res=0
    for i in range(1,len(toys)+1):
        if sum(toys[:i])<k:
            continue
        else:
            res=i-1
            return res



if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        [n,k]=list(map(int,input().split()))
        toys=list(map(int,input().split()))
        ans=solution(toys,k)
        print(ans)