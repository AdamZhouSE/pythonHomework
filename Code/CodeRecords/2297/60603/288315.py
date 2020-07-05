num=int(input())
string=input()
level=int(input())
ans=0
if(level==1):
    if(num==0):
        ans=0
    else:
        ans=1
        time=1
else:
    beforenum=0
    thisnum=0
    nextnum=0

    for i in range(0,level-1):
        beforenum+=int(pow(2,i))

    thisnum=beforenum+int(pow(2,level-1))
    if(beforenum>=num):
        ans=0
    elif(num>=thisnum):
        ans=beforenum+1
        time=int(pow(2,level-1))
    else:
        ans=beforenum+1
        time=num-beforenum
if(ans==0):
    print("EMPTY")
else:
    for i in range(ans,ans+time):
        if(i==(ans+time-1)):
            print(i)
        else:
            print(i,"",end="")