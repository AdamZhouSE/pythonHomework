def exam12():
    s=input()
    if(s=="25"):
        print(1)
        return
    if (s!="2525"):
        print(s)
    n=0
    for i in range(len(s)+1):
        if i==len(s)-1:
            break;
        if ((s[i]=="2")&(s[i+1]=="5")):
            n+=1
        if ((s[i]=="2")&(s[i+1]!="5")):
            print(-1)
            return;
    print(n)
exam12()