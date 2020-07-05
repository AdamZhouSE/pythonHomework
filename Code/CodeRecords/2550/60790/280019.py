l1=input().split()
n=int(l1[0])
m=int(l1[1])
lamp=[0]*n
for i in range(0,m):
    action=input().split()
    action=list(map(int,action))
    if(action[0]==0):
        begin=action[1]-1
        end=action[2]
        for j in range(begin,end):
            if(lamp[j]==0):
                lamp[j]=1
            else:
                lamp[j]=0
    else:
        begin=action[1]-1
        end=action[2]
        print(sum(lamp[begin:end]))