test=list(input())
lst=[]
for x in test:
    if x!="," and x!="[" and x!="]":
        lst.append(x)
lst=sorted(lst)
if len(lst)<2:
    print(0)
else:
    m=int(lst[1])-int(lst[0])
    for i in range(len(lst)-1):
        if (int(lst[i+1])-int(lst[i]))>=m:
            m=int(lst[i+1])-int(lst[i])
    print(m)
