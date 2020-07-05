num=int(input())
data=list(map(int,input().split()))
numof5=data.count(5)
numof0=data.count(0)
if numof0<1:
    print(-1)
elif numof5<9:
    print(0)
else:
    setof5=int(numof5/9)
    s=''
    for i in range(setof5):
        s+='555555555'
    for j in range(numof0):
        s+='0'
    res=int(s)
    print(res)