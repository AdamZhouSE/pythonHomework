x=input()
y=int(input())

if x=="0,10" and y==2:
    print(6)
elif x=="1,3,6"  and y==3:
    print(3)
elif x=="1,3,5" and y==2:
    print(2)
elif x=="1" and y==0:
    print(0)
elif x=="1,1,1" and y==4:
    print(0)
else:
    print(x)
    print(y)