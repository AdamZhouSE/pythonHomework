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


s=iter(stdin.readline())
flag=0
m=n=[]
time=0
while True:
    temp=next(s,'f')
    if temp=='f' and time<9:
        print("Pending")
        break
    elif temp=='f' and time==9:
        print("Draw")
        break
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