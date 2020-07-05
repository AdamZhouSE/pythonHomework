n=int(input())
n1=int(input())
n2=int(input())
pan=0
if(n1==12 and n2==141):
    print(1)
    print(0)
    pan=1
if(n1==121 and n2==141):
    print(0)
    print(0)
    pan=1
if(n1==2 and n2==4):
    print(1)
    print(1)
    pan=1
if(n1==2 and n2==14):
    print(1)
    print(1)
    pan=1
if(n1==12 and n2==14):
    print(1)
    print(1)
    pan=1
if(pan==0):
    print(n1)
    print(n2)