import sys
from sys import stdin

def check(list,flag):
  if win(list):
    if flag==0:
        print('A')
    else:print('B')
    return True
  else:
        return False
        
def win(list):
    
    return False


x=stdin.readline()[1:]
v=int(len(x)/6)
z=[]
for i in range(0,v):
    z.append(x[i*6:i*6+5])
s=iter(z)

flag=0
m=[]
n=[]
time=0
while True:
    temp=next(s,'f')
    if temp=='f' and time<9:
        print("Pending")
        sys.exit(0)
    elif temp=='f' and time==9:
        print("Draw")
        sys.exit(0)
    else:
        time+=1
        if flag==0:
            m.append(temp)
            if check(m,0):
                break
        else:
            n.append(temp)
            if check(n,1):
                break
        flag=1-flag