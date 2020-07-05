def pow(n):
    pro=1
    if n>0:
        for i in range(n):
            pro*=2
    return pro
def getLevel(n):
    level=1
    sum=2
    while sum<n:
        level+=1
        sum+=pow(level)
    return level
def resultStr(n):
    result=""
    level=getLevel(n)
    beginning=0
    for i in range(1,level):
        beginning+=pow(i)
    ind=n-beginning
    for i in range(1,level+1):
        if ind % pow(i) <= pow(i - 1) and ind % pow(i) != 0:
            result =  '4'+result
        else:
            result = '7'+result
    return result
t=int(input())
for i in range(t):
    n=int(input())
    print(resultStr(n))