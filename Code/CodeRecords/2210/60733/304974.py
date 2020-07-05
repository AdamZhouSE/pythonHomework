from collections import defaultdict
for _ in range(int(input())):
    s=input()
    t=input()
    if len(t)>len(s):
        print(-1)
        continue
    d=defaultdict(int)
    c=defaultdict(int)
    n=len(t)
    c0=0
    a=0
    x=-1
    m=111111111
    for i in s:
        d[i]=0
        c[i]=0
    for i in t:
        c[i]+=1
    #print(c)
    #print(d)
    for i in range(len(s)):
        d[s[i]]+=1
        if d[s[i]]!=0 and d[s[i]]<=c[s[i]]:
            c0+=1
        if c0==n:
            while d[s[a]]>c[s[a]] or c[s[a]]==0:
                if d[s[a]]>c[s[a]]:
                    d[s[a]]-=1
                a+=1
            len_window = i - a + 1
            if m > len_window:  
                m = len_window  
                x=a
    if x==-1:
        print(-1)
    else:
        print(s[x:(x+m)])
                
               

    
    


