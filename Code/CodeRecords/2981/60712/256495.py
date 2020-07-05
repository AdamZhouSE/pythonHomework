
import re
p =list(map(int,input().split()))
s=re.split(r"([-])",input())
for i in range(len(s)):
    if s[i]=='-':

        pre = list(s[i-1])
        pres =0
        post=list(s[i+1])
        posts=0

        if 'a'<=pre[len(pre)-1]<='z':
            pres=1
        else:
            pres=2
        if 'a'<=post[0]<='z':
            posts=1
        else:
            posts=2
        if pres==posts and pre[len(pre)-1]<post[0]:
            preascii=ord(pre[len(pre)-1])
            postascii = ord(post[0])
            if postascii - preascii>1:
                s2=""
                start=0
                end=0
                x=0
                if p[2]==1:
                    start = 1
                    end = postascii-preascii
                    x=1
                else:
                    start=postascii-preascii-1
                    end=0
                    x=-1
                for j in range(start,end,x):
                    for k in range(p[1]):
                        if p[0]==2 and pres==1:
                            s2=s2+chr(preascii+j).upper()
                        elif p[0]==3:
                            s2=s2+'*'
                        else:
                            s2=s2+chr(preascii+j)
                s[i]=s2
print("".join(s))






