def  solution(rag):
    cnt=0
    if len(str(rag[0]))==1:
        if len(str(rag[1]))==1:
            cnt+=(rag[1]-rag[0]+1)
            return cnt
        else:
            cnt+=(9-rag[0]+1)
    tmp=rag[1]//11
    cnt+=tmp
    return cnt

if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        rag = list(map(int, input().split()))
        ans=solution(rag)
        print(ans)