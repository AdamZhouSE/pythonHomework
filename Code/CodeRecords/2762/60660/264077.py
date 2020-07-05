import re
class Map:
    d=['N','E','S','W']
    x=0
    y=0
    dir=0
    rl={"R":1,"L":-1,'U':0,'D':2}
    def move(self, dr, length):
        l=int(length)
        self.dir=(self.dir+self.rl[dr])%4
        if self.dir==0:
            self.y+=l
        elif self.dir==1:
            self.x+=l
        elif self.dir==2:
            self.y-=l
        else:
            self.x-=l
    def print(self):
        print(int((self.x**2+self.y**2)**0.5),self.d[self.dir])
t=int(input())
for i in range(t):
    n=int(input())
    m=Map()
    s=input()
    d=re.findall('[A-Z]',s)
    l=re.findall('[0-9]',s)
    for j in range(0,len(l)):
        m.move(d[j],l[j])
    m.print()