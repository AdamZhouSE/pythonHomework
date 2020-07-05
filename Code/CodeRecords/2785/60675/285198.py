n = eval(input())
ai = []
def trying(x,n,ai,degree):
    if x==n:
        return degree%360==0
    return trying(x+1,n,ai,degree+ai[x])|trying(x+1,n,ai,degree-ai[x])
for i in range(0,n):
    ai.append(eval(input()))
if trying(0,n,ai,0):
    print('YES')
else:
    print('NO')
