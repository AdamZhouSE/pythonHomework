a=int(input())
b=input().split(' ')
for i in range(0,len(b)):
    b[i]=int(b[i])
if len(b)==1:
    if(b[0]==15):
        print("DOWN")
    elif(b[0]==0):
        print("UP")
    else:
        print(-1)
else:
    if (b[len(b) - 1] > b[len(b) - 2]):
        if (b[len(b) - 1] == 15):
            print("DOWN")
        else:
            print("UP")
    else:
        if (b[len(b) - 1] == 0):
            print("UP")
        else:
            print("DOWN")