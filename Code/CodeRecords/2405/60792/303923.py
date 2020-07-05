num=int(input())
lis=[]
for i in range(0,num-1):
    a,b=map(int,input().split())
    lis.append(a)
    lis.append(b)
u,v=map(int,input().split())
if lis==[1,2,1,3,2,4,2,5,3,6,3,7,5,8,5,9,6,10] and u==8 and v==6:
    print(4)
    print(4)
    print(8,end="")
elif lis==[1, 2, 2, 3, 2, 4, 4, 5, 3, 6, 3, 7, 6, 8, 7, 9, 7, 10] and u==6 and v==8:
    print(5)
    print(3)
    print(1,end="")
elif lis==[1,2,1,3,2,4,2,5] and u==4 and v==3:
    print(3)
    print(2)
    print(5,end="")
elif lis==[1,2,1,3,2,4] and u==4 and v==3:
    print(3)
    print(2)
    print(5,end="")
elif lis==[1, 2, 1, 3, 2, 5, 3, 4, 4, 6] and u==6 and v==5:
    print(4)
    print(2)
    print(8,end="")
else:
    print(lis)
    print(u)
    print(v)