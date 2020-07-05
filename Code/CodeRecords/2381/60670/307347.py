def int2neg2(x):
    x=int(input())
    ans=""
    while x!=0:
        tmp=abs(x%(-2))
        ans+=str(tmp)
        x=(x-tmp)//(-2)
    return "".join(reversed(ans))

def neg22int(arr):
    answer=0
    base=1
    for i in range(len(arr)-1,-1,-1):
        if arr[i]==1:
            answer+=base
        base*=(-2)
    return answer

arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
print(list(int2neg2(neg22int(arr1)+neg22int(arr2))))