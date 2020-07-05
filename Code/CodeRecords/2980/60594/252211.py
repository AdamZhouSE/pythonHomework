s=(list)(input())
edit=(list)(input().replace(" ",""))
oc=""
if edit[0]=="D":
    for index in range(len(s)):
        if s[index]==edit[1]:
            del s[index]
            break
    for index in range(len(s)):
        oc=oc+s[index]
    print(oc)
elif edit[0]=="I":
    biaoji=0
    for index in range(len(s)):
        if s[index]==edit[1]:
            biaoji=index
    for index in range(len(s)):
        if index==biaoji:
            oc=oc+edit[2]
        oc=oc+s[index]
    print(oc)
elif edit[0]=="R":
    biaoji=-1
    for index in range(len(s)):
        if s[index]==edit[1]:
            s[index]=edit[2]
            biaoji=index
    for index in range(len(s)):
        oc=oc+s[index]
    if biaoji==-1: 
        print("no exist")
    print(oc)