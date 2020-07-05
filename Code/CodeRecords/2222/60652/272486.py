s=input().replace('-','+-')
l,r=s.split('=')
def f(s):
    if '+' in s:
        a=list(s.split('+'))
    else:
        a=[s]
    num=0
    x=0
    for i in a:
        if 'x' in i:
            if i=='x':
                x+=1
            else:
                tmp=i.replace('x','')
                x+=int(tmp)
        else:
            num+=int(i)
    return [x,num]
left=f(l)
right=f(r)
x=left[0]-right[0]
n=right[1]-left[1]
if x==0:
    if n==0:
        print("Infinite solutions")
    else:
        print("No solution")
else:
    if n%x==0:
        print('x='+str(n//x))
    else:
        print('x='+str(n/x))