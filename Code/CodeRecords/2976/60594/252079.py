s=(list)(input().replace(" ",""))
while True:
    try:
        n=(list)(input().replace(" ",""))
        oc=""
        index1=0
        while index1<len(n):
            if index1<len(n)-len(s)+1:
                if (n[index1]+"").upper()==(s[0]+"") or (n[index1]+"").lower()==(s[0]+""):
                    zj=index1
                    shifou=True
                    for index2 in range(len(s)):
                        if s[index2].upper()!=n[zj] and s[index2].lower()!=n[zj]:
                            shifou=False
                            break
                        else:
                            zj+=1
                    if shifou==True:
                        index1+=len(s)
                    else:
                        oc=oc+n[index1]
                        index1+=1
                else:
                    oc=oc+n[index1]
                    index1+=1
            else:
                oc=oc+n[index1]
                index1+=1
        print(oc)
    except EOFError:
        break
