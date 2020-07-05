def solution(s):
    st=set(s)
    if len(st)==len(s):
        return -1
    dt={}
    for i in s:
        if i not in dt:
            dt[i]=1
        else:
            dt[i]+=1
    maxchrs=[]
    for key,value in dt.items():
        fst=s.find(key)
        start=fst
        for cnt in range(value-1):
            p=s.find(key,start+1)
            start=p+1
        gap=start-1-fst-1
        maxchrs.append(gap)
    return max(maxchrs)

if __name__=="__main__":
    n=int(input())
    for _ in range(n):
        s=input()
        ans=solution(s)
        print(ans)