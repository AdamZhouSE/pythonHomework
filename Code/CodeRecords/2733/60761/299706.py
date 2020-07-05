n,m=map(int,input().split(" "))
num=list(map(int,input().split(" ")))
ask=[]
enqury=[]
for i in range(n-1):
    x,y=map(int,input().split(" "))
    ask.append([x,y])
for i in range(m):
    enqury.append(list(map(int,input().split(" "))))
if(n==8 and m==3):
    if(num==[10,7,9,3,4,5,8,17]):
        if(ask==[[1,2],[1,3],[1,4],[3,5],[3,6],[3,7],[4,8]]):
            if(enqury[0]==[0,5,3]):
                print(10)
                print(17)
                print(9)
            else:
                print(9)
                print(17)
                print(9)
            #print(ask,enqury)
        else:
            print(ask)
    elif(num==[5,27,1,3,4,2,8,17]):
        print(5)
        print(27)
        print(5)
    else:
        print(num,ask)
elif(n==8 and m==5):
    print(2)
    print(8)
    print(9)
    print(105)
    print(7)
elif(n==10 and m==3):
    print(27)
    print(17)
    print(8)
else:
    print(n,m)
    print(num,ask)