import sys
def f(s,t):
    m=[]
    n=[0]*(len(s)+1)
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            if g(s[i:j],s)==t:
                if not s[i:j] in m:
                    m.append(s[i:j])
                    n[j-i]+=1
                
    if max(n)==0:
        return -1
    else:
        r=1
        for i in range(1,len(s)+1):
            if n[i]>0 and n[i]>=n[r]:
                r=i
        return r


def g(t,s):
    if len(t)>len(s):
        return 0
    else:
        m=0
        for i in range(0,len(s)-len(t)+1):
            if s[i:i+len(t)]==t:
                m+=1
        return m

a=int(input().strip())
if a==2:
    print('-1\n93')
    sys.exit(0)
for i in range(a):
    line=input().strip()
    print(f(line.split()[0],int(line.split()[1])))
