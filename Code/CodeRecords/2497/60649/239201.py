n=int(input())
pos=input()
speed=input()
count=0
pos=pos[1:len(pos)-1]
speed=speed[1:len(speed)-1]
pos=list(map(int,pos.split(",")))
speed=list(map(int,speed.split(",")))
lst=sorted(zip(pos,speed),reverse=True)
for i in range(0,len(pos)-1):
    if (n-pos[i])/speed[i]>=(n-pos[i+1])/speed[i+1]:
        count+=1
print(count)
