def f(s,t):
    max=-1
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            if g(s[i:j],s)==t and j-i>max:
                max=j-i
    return max


def g(t,s):
    if len(s)>len(t):
        return 0
    else:
        m=0
        for i in range(0,len(s)-len(t)+1):
            if s[i:i+len(t)]==t:
                m+=1
        return m

a=int(input().strip())
for i in range(a):
    line=input().strip()
    print(f(line.split()[0],int(line.split()[1])))
