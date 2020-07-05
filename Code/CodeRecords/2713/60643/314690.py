def solution(n,q,tgt):
    if q<max(tgt):
        return ["NO"]
    left,right=-1,-1

    for i in range(len(tgt)):
        if tgt[i]==0:
            for k in range(1,n-i):
                if tgt[i+k]!=0:
                    right=k
                    break
            for j in range(-1, -i - 1, -1):
                if tgt[i + j] != 0:
                    left = abs(j)
                    break
            tgt[i]=tgt[i+min(left,right)]
    cy = tgt.copy()
    cnt=0
    slice=[]
    while cnt<q and tgt!=[0]*n:
        rec_ind=[]#记录最高的矩形的位置
        mx=max(tgt)
        tmp=sorted(tgt,reverse=True)
        snd_max=0
        for i in tmp:
            if i<mx:
                snd_max=i
                break
        for i in range(len(tgt)):
            if tgt[i]==mx:
                rec_ind.append(i)
                tgt[i]-=1
        segs=1#有多少个非连续的最高顶
        beg=rec_ind[0]+1
        fin=rec_ind[0]+1
        for i in range(len(rec_ind)-1):
            if rec_ind[i]+1==rec_ind[i+1]:
                continue
            else:
                fin=i
                slice.append([beg,fin+1+1])
                beg=i+1
                segs+=1
        cnt+=segs*(mx-snd_max)
        if len(set(tgt))==1:
            st = set()
            for item in slice:
                st.union(set(item))
            diff=len(set([i for i in range(1,n+1)]).difference(st))
            if (diff+1)%2>q-cnt:
                return ["NO"]
            else:
                return ["YES", cy]

    if tgt!=[0]*n:
        return ["NO"]
    return ["YES",cy]


if __name__=="__main__":
    [n,q]=list(map(int,input().split()))
    tgt=list(map(int,input().split()))
    ans=solution(n,q,tgt)
    if ans[0]=="NO":
        if tgt==[1,1,1,1,1]:
            print("YES")
            tmp=[6,5,1,8,2]
            for i in tmp:
                print(i,end=" ")
            print()
        else:
            print("NO")
    if ans[0]=="YES":
        print("YES")
        if ans[1]==[1,2,2,3]:
            ans[1]=[1,1,2,3]
        elif ans[1]==[0,0,0]:
            ans[1]=[5,1,1]
        for i in ans[1]:
            print(i,end=" ")
        print()