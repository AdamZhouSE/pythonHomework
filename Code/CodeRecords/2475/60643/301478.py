def  solution(n,a):
    maxLen=1
    a=sorted(a)

    for i in range(len(a)-1):
        for j in range(i+2,len(a)+1):
            flag=False
            tmp=a[i:j]
            for k in range(len(tmp)-1):
                if tmp[k+1]!=tmp[k]+1:
                    maxLen=max(maxLen,k-0+1)
                    flag=True
                    break
            if flag:
                break
    res=maxLen
    return res


if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        ans=solution(n,a)
        print(ans)