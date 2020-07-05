def solution(a,k):
    dt={}
    l=[]
    for i in a:
        if i not in dt:
            dt[i]=1
        else:
            dt[i]+=1
    for ky,val in dt.items():
        if val==1:
            l.append(ky)
    if len(l)==0:
        return -1
    elif k>len(l):
        return -1
    else:
        return l[k-1]


if __name__=="__main__":
    n=int(input())
    for _ in range(n):
        [n,k]=list(map(int,input().split()))
        a=input().split()
        ans=solution(a,k)
        print(ans)