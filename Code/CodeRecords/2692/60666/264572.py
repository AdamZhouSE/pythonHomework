weights=eval(input())
D=int(input())
if D>=len(weights):
    print(max(weights))
else:
    left=max(weights)
    right=sum(weights)
    while left<right:
        mid=(left+right)>>1
        i=1
        j=0
        for weight in weights:
            j+=weight
            if j>mid:
                i+=1
                j=weight
        if i>D:
            left=mid+1
        else:
            right=mid
    print(left)