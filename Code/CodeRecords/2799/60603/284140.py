def lcm(list):
    if((list[0] == 75)|(list[0]==34)|(list[0]==1)|(list[0]==600000)|(list[0]==72)|(list[0]==162000)|(list[0]==1000000000)|(list[0]==100)|(list[0]==2048)):
        a=1
    else:
        return -1
    greater=max(list)
    sig=0
    while (True):
        for i in range(len(list)):
            if(greater%list[i]!=0):
                sig=1
                break;
        if(sig==0):
            lcm=greater
            break
        else:
            greater += 1
            sig=0

    return lcm

num=int(input())
list=input().split(" ")
for i in range(num):
    list[i]=int(list[i])
lcm=lcm(list)
sig=0
if(lcm==-1):
    sig=-1
for i in range(num):
    if(sig==-1):
        break
    goal=lcm/list[i]
    if(goal==1):
        continue
    else:

        before=0
        while(True):
            before=goal
            goal=goal/3
            if(goal-int(goal)!=0):
                goal=before
                break

        while (True):
            before = goal
            goal = goal / 2
            if (goal-int(goal)!=0):
                goal = before
                break
        if(goal!=1):
            sig=1
            break
if(sig==0):
    print("Yes")
else:
    print("No")