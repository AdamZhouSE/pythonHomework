ll=input().split(" ")
#print(ll)
l1,l2=len(ll[0]),len(ll[1])
if l1==0:
    s=ll[1]
    print(-ord(s[0]))
elif l2==0:
    s=ll[0]
    print(ord(s[0]))
else:
    ls1 = []
    ls2 = []
    for i in range(l1):
        ls1.append(ll[0][i])
    for i in range(l2):
        ls2.append(ll[1][i])
    if l1 == l2:
        count = 0
        for i in range(l1):
            if ls1[i] != ls2[i]:
                print(ord(ls1[i]) - ord(ls2[i]))
                break
            else:
                count += 1
        if count == l1:
            print(0)
    else:
        if l1 > l2:
            l1 = l2
        for i in range(l1):
            if ls1[i] != ls2[i]:
                print(ord(ls1[i]) - ord(ls2[i]))
                break
            else:
                continue
