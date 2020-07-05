n=int(input())
temp=[int(x) for x in input().split(' ')]

last=len(temp)-1

if(len(temp)==1):
    if(temp[0]==0):
        print("UP")
    elif(temp[0]==15):
        print("DOWN")
    else:
        print(-1)
elif(temp[last]==15):
    print("DOWN")
elif(temp[last]>temp[last-1]):
    print("UP")
elif(temp[last]==0):
    print("UP")
else:
    print("DOWN")
    