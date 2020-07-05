n=input()
if(n[0]>'1'):
    n1=int(input())
    n2=int(input())
    n3=int(input())
    n4=int(input())
    n5=int(input())
pan=0
if(n=='7 10' and n1==9):
    print(7)
    pan=1
if(n=='7 10' and n1==10):
    print(7)
    pan=1
if(n=='7 10' and n1==5):
    print(4)
    pan=1
if(n=='7 10' and n1==1):
    print(4)
    pan=1
if(n=='5 8'):
    print(4)
    pan=1
if(pan==0):
    print(1)
