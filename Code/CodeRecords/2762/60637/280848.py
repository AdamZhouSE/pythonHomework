tests=(int)(input())
d=['N','E','S','W']
def turn(mov,direction):
    global d
    l=d.index(direction)
    if(mov=='D'):
        return d[(l+2)%4]
    elif(mov=='R'):
        return d[(l+1)%4]
    elif(mov=='L'):
        return d[(3+l)%4]
    return direction
def move(x,y,mov,distance,direction):
    direction=turn(mov,direction)
    if(direction=='N'):
        y+=distance
    elif(direction=='S'):
        y-=distance
    elif(direction=='W'):
        x-=distance
    else:
        x+=distance
    return [x,y,direction]
for i in range(tests):
    step_num=(int)(input())
    steps=input().split(' ')
    coordinate=[0,0,'N']
    for i in range(step_num):
        coordinate=move(coordinate[0],coordinate[1],steps[0+2*i],(int)(steps[1+2*i]),coordinate[2])
    print((int)(pow(pow(coordinate[0],2)+pow(coordinate[1],2),1/2)),coordinate[2])
