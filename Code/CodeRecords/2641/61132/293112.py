s1=list(input())
s2=list(input())
l1=len(s1)
l2=len(s2)
if l1>l2:
    print(False)
else:
    index=0
    while index+l1<=l2:
        if set(s1)==set(s2[index:index+l1]):
            print(True)
            break
        index+=1
    else:
        print(False)