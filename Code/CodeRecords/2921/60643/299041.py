def solution(data,d):
    st=set()
    for i in data:
        if i%d not in st:
            st.add(i%d)
    if len(st)>1:
        return -1
    else:
        data=sorted(data)
        ind=len(data)//2
        tgt=data[ind]
    cnt=0
    for i in data:
        cnt+=abs((i-tgt))//d
    return cnt

if __name__=="__main__":
    [n,m,d]=list(map(int,input().split()))
    data=[]
    for _ in range(n):
        tmp=list(map(int,input().split()))
        data.extend(tmp)
    ans=solution(data,d)
    print(ans)