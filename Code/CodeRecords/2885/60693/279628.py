def mergeArray(arr:list):
    res=0
    after1,after2=0,0
    for x in arr:
        if not x%3:
            res+=1
        elif x%3==1:
            after1+=1
        else:
            after2+=1
    res+=min(after1,after2)
    left=max(after1,after2)-min(after1,after2)
    res+=left//3
    return res

cases=int(input())
for _ in range(cases):
    n=int(input())
    arr=list(map(int,input().split()))
    print(mergeArray(arr))