def exam12():
    s=input()
    n=0
    for i in range(len(s)+1):
        if i==len(s)-1:
            break;
        if ((s[i]=="2")&(s[i+1]=="5")):
            n+=1
    print(n)
exam12()