class man():
    def __init__(self):
        self.x,self.y,self.s=0,0,'N'

    def go(self,d):
        dx={
            'N':0,
            'S':0,
            'W':-d,
            'E':d
        }[self.s]
        dy={
            'N':d,
            'S':-d,
            'W':0,
            'E':0
        }[self.s]
        self.x+=dx
        self.y+=dy

    def back(self,d):
        dx={
            'N':0,
            'S':0,
            'W':d,
            'E':-d
        }[self.s]
        dy={
            'N':-d,
            'S':d,
            'W':0,
            'E':0
        }[self.s]
        ns={
            'N': 'S',
            'S': 'N',
            'W': 'E',
            'E': 'W'
        }[self.s]
        self.x+=dx
        self.y+=dy
        self.s=ns

    def left(self,d):
        dx={
            'N':-d,
            'S':d,
            'W':0,
            'E':0
        }[self.s]
        dy={
            'N':0,
            'S':0,
            'W':-d,
            'E':d
        }[self.s]
        ns={
            'N': 'W',
            'S': 'E',
            'W': 'S',
            'E': 'N'
        }[self.s]
        self.x+=dx
        self.y+=dy
        self.s=ns

    def right(self,d):
        dx={
            'N':d,
            'S':-d,
            'W':0,
            'E':0
        }[self.s]
        dy={
            'N':0,
            'S':0,
            'W':d,
            'E':-d
        }[self.s]
        ns={
            'N': 'E',
            'S': 'W',
            'W': 'N',
            'E': 'S'
        }[self.s]
        self.x+=dx
        self.y+=dy
        self.s=ns

    def show(self):
        d=int((self.x**2+self.y**2)**0.5)
        print(d,self.s)

def solve():
    n=int(input())
    ops=input().split()
    tom=man()
    for i in range(n):
        op=ops[2*i]
        d=int(ops[2*i+1])
        if op=='U':
            tom.go(d)
        elif op=='D':
            tom.back(d)
        elif op=='L':
            tom.left(d)
        else:
            tom.right(d)
    tom.show()

if  __name__ == '__main__' :
    total=int(input())
    for _ in range(total):
        solve()