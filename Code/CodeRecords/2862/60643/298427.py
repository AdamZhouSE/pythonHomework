def solution(lst):
    odd=[x for x in lst if x%2!=0]
    even=[x for x in lst if x%2==0]
    l1=len(odd)
    l2=len(even)
    if l1==0:
        return sum(even[1:])
    elif l2==0:
        return sum(odd[1:])
    odd=sorted(odd,reverse=True)
    even=sorted(even, reverse=True)

    if l1==l2 or abs(l1-l2)==1:
        return 0
    else:
        if l1>l2:
            res=odd[l2+1:]
        else:
            res=even[l1+1:]
        return sum(res)

if __name__=="__main__":
    n=int(input())
    lst=list(map(int,input().split()))
    ans=solution(lst)
    print(ans)