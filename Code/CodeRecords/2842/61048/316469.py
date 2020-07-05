def arr39():
    n=int(input())
    set=[]
    res=0
    for i in range(n):
        set.append(int(input()))
    cnt=1
    for i in range(n):
        f=set[i]
        while(f!=-1):
            cnt+=1
            f=set[f-1]
        res=max(cnt,res)
        cnt=1
    print(res)
    return 

arr39()