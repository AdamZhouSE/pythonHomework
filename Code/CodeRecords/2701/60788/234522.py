from sys import stdin

def check(list,flag):
  if win(list):
    if flag==0:
        print('A')
    else:print('B')
        
def win(list):
    return False


s=iter(stdin.readline(),'f')
flag=0
m=n=[]
while True:
    temp=next(s)
    if temp=='f':
        print("Pending")
        break
    else:
        if flag==0:
            m.append(temp)
            check(m,0)
        else:
            n.append(temp)
            check(n,1)
        flag=1-flag