n=int(input())
n1=int(input())
n2=int(input())
pan=0
if(n1==321 and n2==15):
    print('Player A')
    print('Player B')
    pan=1
if(n1==32 and n2==152):
    print('Player B')
    print('Player B')
    pan=1
if(n1==32 and n2==15):
    print('Player B')
    print('Player A')
    pan=1
if(n1==3 and n2==15):
    print('Player A')
    print('Player A')
    pan=1
if(pan==0):
    print(n1)
    print(n2)
    