if __name__=="__main__":
    n,k=input().split()
    n=int(n)
    k=int(k)
    weight=input().split()
    weight=[int(x) for x in weight]
    cnt=0
    for i in range(len(weight)):
        if weight[i]<=k:
            cnt+=1
        else:
            break
    if cnt!=len(weight):
        for i in range(len(weight)-1,0,-1):
            if weight[i]<=k:
                cnt+=1
            else:
                break
    print(cnt)