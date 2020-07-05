n=int(input())
result=0
def su(n):
    if(n==2):
        return True
    for i in range(2,n):
        if(n%i==0):
            return False
    return True
def hui(n):
    a=[]
    s=list(str(n))
    a.extend(s)
    s.reverse()
    if(a==s):
        return True
    return False
for i in range(n,2*10**8):
    if(su(i) and hui(i)):
        result=i
        break
print(result)
        