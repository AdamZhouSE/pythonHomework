def solution(a:list,b:list):
    getIn=[]
    overtake=[False]*len(a)#记录该车有没有超车 （不是被超车）
    cnt=0
    for car in a:
        if car not in getIn:
            getIn.append(car)
        p=b.index(car)
        for i in range(p):
            if b[i] not in getIn and not overtake[i]:
                cnt+=1
                overtake[i]=True
    return cnt

if __name__=="__main__":
    n=int(input())
    a=list(map(int,input().split()))
    b = list(map(int, input().split()))
    ans=solution(a,b)
    print(ans)