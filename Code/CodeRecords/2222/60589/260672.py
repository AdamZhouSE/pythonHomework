eq=input().split('=')
num_x=0
n=0
left=eq[0]
left=left.replace('-','+-')
left=left.split('+')
for a in left:
    if 'x' in a:
        if a=='x':
            a='1x'
        elif a=='-x':
            a='-1x'
        num_x+=int(a[:-1])
    else:
        n-=int(a)
right=eq[1]
right=right.replace('-','+-')
right=right.split('+')
for a in right:
    if 'x' in a:
        if a=='x':
            a='1x'
        elif a=='-x':
            a='-1x'
        num_x-=int(a[:-1])
    else:
        n+=int(a)
if num_x==0 and n==0:
    print('Infinite solutions')
elif num_x==0:
    print('No solution')
else:
    print('x='+str(n/num_x))