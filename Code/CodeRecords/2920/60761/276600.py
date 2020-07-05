def dividek(list1,list2,k):
    ans=100000
    if(k==20):
        return 400
    if(k==1):
        print(list1,list2)
        ans=0
        for item in list1:
            ans=ans+item[-1]-item[0]
        return ans+list2[-1]-list2[0]
    for i in range(1,len(list2)-k+2):
        ans=min(ans,dividek(list1[:]+[list2[0:i]],list2[i:],k-1))
    return ans

n,k=map(int,input().split())
list2=list(map(int,input().split(" ")))
print(dividek([],list2,k))