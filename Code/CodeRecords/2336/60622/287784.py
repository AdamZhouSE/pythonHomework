n=int(input())
for x in range(n):
    l=list(map(int,input().split()))
    k=l[1]
    arr=list(map(int,input().split()))
    ans=[]
    for i in range(len(arr)-(k-1)):
        tem=[]
        for j in range(k):
            tem.append(arr[i+j])
        tem.sort()
        ans.append(tem[-1])
    for e in ans:
        print(e,end=" ")
    print()