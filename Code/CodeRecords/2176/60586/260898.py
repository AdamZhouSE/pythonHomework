def exam10():
    s=list(input())
    sc=s.copy()
    sign=[]
    for i in range(len(s)):
        sign.append(True)
    n=[]
    sc.sort()
    for item in sc:
        for i in range(len(s)-1,-1):
            if s[i]==item and sign[i]==True:
                n.append(i)
                sign[i]=False
    string=n[0]
    for i in range(1,len(string)):
        string=string+" "+n[i]
    print(string)print(input())
exam10()