def solution(box):
    box=sorted(box)
    visited=[False]*len(box)
    total=len(box)
    ans=0
    while total>0:
        tmp=0
        for i in range(len(box)):
            if box[i]>=tmp and not visited[i]:
                visited[i]=True
                tmp+=1#下一层需要的最小抗压值
                total-=1# box用了一个
        ans+=1#一个堆建立
    return ans


if __name__=="__main__":
    n=int(input())
    box=input().split()
    box=[int(x) for x in box]
    ans=solution(box)
    print(ans)