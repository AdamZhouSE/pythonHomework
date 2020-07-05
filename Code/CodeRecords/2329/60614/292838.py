def check(a,b):
    if a<b:
        temp=a
        a=b
        b=temp
    while a%b!=0:
        temp=a%b
        a=b
        b=temp
    if b>1:
        return True
    else:
        return False
nums=[int(x) for x in input().split(',')]
groups=[[x] for x in nums]
for i in nums:
    j=0
    while j<len(groups):
        if i not in groups[j]:
            for k in groups[j]:
                if check(k,i):
                    for l in range(len(groups)):
                        if i in groups[l]:
                            groups[j]=groups[j]+groups[l]
                            del groups[l]
                            j-=1
                            break
                    break
        j+=1
maximum=0
for i in groups:
    maximum=max(maximum,len(i))
print(maximum)