input()
list2=list(map(int,input().split(' ')))
res=0
i=0
while i<len(list2):
    mask=list2[i]
    temp=i
    while i<len(list2):
        if list2[i]!=mask:
            break
        i+=1
    cnt1=i-temp
    mask=list2[i]
    temp=i
    while i<len(list2):
        if list2[i]!=mask:
            break
        i+=1
    cnt2=i-temp
    res=max(min(cnt1,cnt2)*2,res)
    if i!=len(list2):
        i=temp
print(res)