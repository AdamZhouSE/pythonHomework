def func(a):
    if(a==0 ):
        return 0
    elif(a==1):
        return 1
    else:
        if(a%2==0):
            return func(int(a/2))+1
        else:return func(a-1)+1
testnum=int(input())
for i in range(testnum):
    num=int(input())
    print(func(num))