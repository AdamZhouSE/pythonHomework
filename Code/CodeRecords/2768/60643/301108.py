def  solution(a,b,m):
    res=[]
    for i in range(a,b+1):
        if i%m==0:
            res.append(i)
    return len(res)



if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        [a,b,m]=list(map(int,input().split()))
        ans=solution(a,b,m)
        print(ans)