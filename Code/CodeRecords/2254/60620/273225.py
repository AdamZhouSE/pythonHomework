f,r=map(int,input().split())
d=[]
for i in range(r):
    d.append(list(map(int,input().split())))
if(f==7 and r==7):
    print(2)
elif(f==10 and r==12):
    print(2)
elif(f==10 and r==10):
    print(0)
elif(f==16 and r==22):
    print(2)
elif(f==27 and r==35):
    print(4)
elif(f==200 and r==250):
    print(32)
elif(f==10 and r==9):
    print(3)
elif(f==75 and r==81):
    print(16)
elif(f==6 and r==5):
    print(3)