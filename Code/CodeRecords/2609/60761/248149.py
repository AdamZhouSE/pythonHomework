def kthInt(numlist,k):
    numset=set(numlist)
    if(len(numset)<k):
        return "-1"
    else:
        i=k
        for num in numlist:
            if numlist.count(num)==1:
                if num in numset and i>=2:
                    numset.remove(num)
                    i=i-1
                elif num in numset and i==1:
                    return num
        return "-1"
t=int(input())
for i in range(t):
    n,k=map(int,input().split(" "))
    numlist=list(map(int,input().split(" ")))
    print(kthInt(numlist,k))