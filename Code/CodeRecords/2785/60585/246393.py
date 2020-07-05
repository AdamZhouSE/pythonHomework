def trying(i,degree):
    if i==n:
        return degree%360==0
    return trying(i+1,degree+option[i])|trying(i+1,degree-option[i])

n=eval(input())
option=[]
for _ in range(n):
    temp=eval(input())
    option.append(temp)
if trying(0,0):
    print('YES')
else:
    print('NO')