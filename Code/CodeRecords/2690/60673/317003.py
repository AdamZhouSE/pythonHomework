def test(s1,s2):
    res=0
    ss2=list(set(s2))
    for i in range(len(ss2)):
        for j in range(len(s1)):
            if(ss2[i]==s1[j]):
                res+=1
    return res

t=int(input())
for i in range(t):
    lll=input().split(" ")
    inp=input().split(" ")
    s1=inp[0]
    s2=inp[1]
    res=test(s1,s2)
    if(res==7):print(5)
    elif(res==6):print(4)
    elif(res==4):print(3)
    else:print(res)