list0=input().split(',')
list0=[int(list0[i]) for i in range(len(list0))]
list0.sort()
count=list0[0]+1
size=list0[0]+1
base=1
for i in range(1,len(list0)):
    if list0[i]==size-1:
        if base+1<=size:
            base+=1
        else:
            count+=list0[i]+1
            base=1
    else:
        base=1
        count+=list0[i]+1
        size=list0[i]+1
print(count)