t=int(input())
def getNum(n):
    result=3
    diff=7
    for i in range(2,n+1):
        result+=diff
        diff+=4
    return result
for i in range(0,t):
    print(getNum(int(input())))