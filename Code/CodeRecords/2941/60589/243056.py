N=int(input())
r=input()
total=0
for c in r:
    if c=="A":
        total+=4
    elif c=='B':
        total+=3
    elif c=='C':
        total+=2
    elif c=='D':
        total+=1
ans=total/N
if total==0:
    print(0,end='')
else:
    print('%.14f'%ans,end='')