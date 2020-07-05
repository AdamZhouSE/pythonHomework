nums=int(input())
for i in range(nums):
    num=int(input())
    moves=input().split(" ")
    direc=["N","E","S","W"]
    d=0
    cur=[0,0]
    def move(dir,step,cur):
        if dir=="W":
            cur[0]-=step
        elif dir=="E":
            cur[0]+=step
        elif dir=="N":
            cur[1]+=step
        else:
            cur[1]-=step
    for j in range(0,num*2,2):
        if moves[j]=="L":
            d=(d+3)%4
            move(direc[d],int(moves[j+1]),cur)
        elif moves[j]=="R":
            d=(d+1)%4
            move(direc[d],int(moves[j+1]),cur)
        elif moves[j]=="D":
            d=(d+2)%4
            move(direc[d],int(moves[j+1]),cur)
        else:
            move(direc[d],int(moves[j+1]),cur)
    print(int(pow(cur[0]**2+cur[1]**2,0.5)),end='')
    print(" "+direc[d])