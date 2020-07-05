up=int(input())
down=int(input())
res=[]

def isnum(n):
    s=str(n)
    if '0' in s:
        return False
    for i in range(len(s)):
        if n%int(s[i])==0:
            continue
        else:
            return False
    return True

for i in range(up, down+1):
    if isnum(i):
        res.append(i)
print(res)

