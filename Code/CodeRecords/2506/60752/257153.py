lst=list(map(int,input().split(',')))
l=1
i=0
end=0
while i<len(lst)-1:
    while lst[end]<lst[i+1]:
        l+=1
        i+=1
        end=i
        if i==len(lst)-1:
    
            break

    i+=1
    if l==1:end=i
if l==2:print(lst)
print(l)