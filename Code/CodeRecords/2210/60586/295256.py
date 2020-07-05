def exam28():
    T = int(input())
    for t in range(T):
        text=input()
        s=input()
        n=len(text)
        string=[]
        length=[]
        for i in range(0,n):
            for j in range(i+1,n+1):
                sub=text[i:j]
                x=True
                for k in range(len(s)):
                    if sub.count(s[k])==0:
                        x=False
                if x:
                    string.append(sub)
                    length.append(len(sub))
        l=length.copy()
        if len(l)==0:
            print(-1)
            return
        l.sort()
        print(string[length.index(l[0])])
exam28()        