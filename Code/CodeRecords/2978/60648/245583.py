s1,s2=input().split("  ")
print(ll)
l1,l2=len(s1),len(s2)
ls1=[]
ls2=[]
for i in range(l1):
    ls1.append(s1[i])
for i in range(l2):
    ls2.append(s2[i])
if l1==l2:
    count=0
    for i in range(l1):
        if ls1[i]!=ls2[i]:
            print(ord(ls1[i])-ord(ls2[i]))
            break
        else:
            count+=1
    if count==l1:
        print(0)
else:
    if l1>l2:
        l1=l2
    for i in range(l1):
        if ls1[i]!=ls2[i]:
            print(ord(ls1[i])-ord(ls2[i]))
            break
        else:
            continue
            