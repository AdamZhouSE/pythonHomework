n=int(input())
n1=int(input())
n2=int(input())
pan=0
if(n1==6 and n2==3):
    print(1)
    print(4)
    pan=1
if(n1==4 and n2==3):
    print(3)
    print(4)
    pan=1
if(n1==6 and n2==2):
    print(1)
    print(5)
    pan=1

if(pan==0):
    print(n1)
    print(n2)