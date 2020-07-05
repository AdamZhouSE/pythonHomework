s=input().split('=')
def cal(s):
    l=[]
    symbol='+'
    xn=0
    nn=0
    for i in s:
        if(i!='+' and i!='-'):
            if(i=='x'):
                numx=1 if len(l)==0 else int(''.join(l))
                if(symbol=='+'):
                    xn+=numx
                else:
                    xn-=numx
                l=[]
            else:
                l.append(i)
        else:
            if(len(l)!=0):
                nn=eval(str(nn)+symbol+''.join(l))
            symbol=i
            l=[]
    if(len(l)!=0):
        nn=eval(str(nn)+symbol+''.join(l))
    return [xn,nn]
left=cal(s[0])
right=cal(s[1])
x=left[0]-right[0]
n=left[1]-right[1]
if(x==0 and n==0):
    print('Infinite solutions')
elif(x==0 and n!=0):
    print('No solution')
else:
    print('x='+str(-n/x))