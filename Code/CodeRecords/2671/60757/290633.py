import math
def judge(s):
    sign=0
    for i in range(len(s)-1):
        if s[i]=='1' and s[i+1]=='1':
            sign=1
            break
    if(sign==0):
        return False
    else:
        return True
def cal(a):
    s=''
    while(a!=0):
        if a%2==1:
            s='1'+s
        else:
            s='0'+s
        a=a//2
    return s
t=int(input())
for i in range(t):
    n=int(input())
    n=int(math.pow(2,n))
    count=0
    for j in range(n):
        if judge(cal(j)):
            count+=1
    print(count)