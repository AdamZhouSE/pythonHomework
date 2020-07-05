lst=list(map(int,input().split(',')))
find=int(input())
index=0
if find<lst[0] or find>lst[len(lst)-1]:print([-1,-1])
else:
    count=lst.count(find)
    if count==0:print([-1,-1])
    else:
        start=0
        end=len(lst)-1
        while True:
            cut=int((start+end)/2)
            if lst[cut]>find:end=cut
            if lst[cut]<find:start=cut
            if lst[cut]==find:
                index=cut
                break
    end=index+count
    while lst[end]!=find:end-=1
    print([end-count+1,end])


