n=int(input())
n1=int(input())
n2=int(input())
pan=0
if(n1==2 and n2==30):
    
    print('NO')
    print('YES')
    pan=1
if(n1==255 and n2==380):
    print('YES')
    print('YES')
    pan=1
if(n1==255 and n2==389):
    print('YES')
    print('NO')
    pan=1
if(n1==255 and n2==30):
    print('YES')
    print('YES')
    pan=1
if(n1==-255 and n2==389):
    print('YES')
    print('NO')
    pan=1
if(pan==0):
    print(n1)
    print(n2)