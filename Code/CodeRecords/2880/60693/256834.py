def out_children(weights:list,n,k):
    left_out,right_out=True,True
    res=0
    i=1
    while (left_out or right_out) and weights:
        if i%2==1 and left_out:
            # 船头
            if weights[0]>k:left_out=False
            else:
                weights.pop(0)
                res+=1
        if i%2==0 and right_out:
            # 船尾
            if weights[-1]>k:right_out=False
            else:
                weights.pop()
                res+=1
        i+=1
    return res

n_k=input().split()
n,k = int(n_k[0]),int(n_k[1])
weights=list(map(int,input().split()))
print(out_children(weights,n,k))