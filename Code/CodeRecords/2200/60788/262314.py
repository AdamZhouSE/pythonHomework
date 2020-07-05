def f(s,t,k):
    good=set()
    for i in range(0,len(s)):
        for j in range(i+1,len(s)+1):
            if is_good(t[i:j],k):
                good.add(s[i:j])
    return len(good)


def is_good(t,k):
    bad=0
    for i in range(len(t)):
        if t[i]=='0':
            bad+=1
    return bad<=k


s=input().strip()
t=input().strip()
k=int(input().strip())
print(f(s,t,k))