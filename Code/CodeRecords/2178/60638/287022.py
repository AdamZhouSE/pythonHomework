n=int(input())
numbers=list(map(int,input().split(" ")))
for i in range(1,n+1):
    res=numbers[0:i]
    result=[]
    for j in  range(1,len(res)+1):
        k=0
        while k+j<=len(res):
            if not result.__contains__(res[k:k+j]):
                result.append(res[k:k+j])
            k=k+1
    print(len(result))