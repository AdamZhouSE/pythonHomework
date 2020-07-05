t=int(input())
def f(n):
    s=list(bin(n))
    s.remove(s[0])
    s.remove(s[0])
    for i in range(len(s)):
        if(i%2==0 and s[i]=='0'):
            return False
        if(i%2==1 and s[i]=='1'):
            return False
    return True
for i in range(t):
    n=int(input())
    result=[]
    for j in range(n):
        if(f(j+1)):
            result.append(j+1)
    print(*result)
    