t=int(input())
for i in range(0,t):
    strr=input()
    patt=input()
    location=-1
    for c in patt:
        tmp=strr.find(c)
        if tmp!=-1:
            if location==-1:
                location=tmp
            elif tmp<location:
                location=tmp
    if location==-1:
        print("$")
    else:
        print(strr[location])
        