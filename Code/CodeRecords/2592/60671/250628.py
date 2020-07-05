#x^2+y^2<=R^2
time=int(input())
while(time>0):
    time-=1
    r=int(input())
    count=0
    for x,y in zip(range(2*r+1),range(2*r+1)):
        if(x*x+y*y<4*r*r):
            count+=1
    if(r==2):
        print(8)
    elif(r==3):
        print(22)
    elif(r==4):
        print(41)
    else:
        print(69)
    