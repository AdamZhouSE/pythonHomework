class location(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.direction=0
    def getx(self):
        return self.x
    def gety(self):
        return self.y
    def setx(self,x):
        self.x=x
    def sety(self,y):
        self.y=y
    def turnLeft(self):
        self.direction=(self.direction+270)%360
    def turnRight(self):
        self.direction=(self.direction+90)%360
    def go(self):
        if self.direction==0:
            self.sety(self.gety()+1)
        elif self.direction==90:
            self.setx(self.getx() + 1)
        elif self.direction==180:
            self.sety(self.gety() - 1)
        else:
            self.setx(self.getx() - 1)


p=location(0,0)

x=input()
x=x+x+x+x
lis=list(x)
for i in lis:
    if i=="G":
        p.go()
    elif i=="L":
        p.turnLeft()
    else:
        p.turnRight()

if p.getx()==0 and p.gety()==0:
    print("true")
else:
    print("false")