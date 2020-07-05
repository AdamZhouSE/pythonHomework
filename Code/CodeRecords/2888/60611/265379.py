num=list(map(int,input().split()))
l=list(map(int,input().split()))
oneNumber=l.count(1)
oneNumberNeg=l.count(-1)
for i in range(num[1]):
    lst=(list(map(int,input().split())))
    if (lst[1]-lst[0]+1)%2!=0:
        print(0)
    elif min(oneNumber,oneNumberNeg)*2>=(lst[1]-lst[0]+1):
        print(1)
    else:
        print(0)