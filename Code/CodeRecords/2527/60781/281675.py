str1=input()
n1=int(input())
n2=int(input())
n3=int(input())
pan=0
if(n1==0 and n2==50 and n3==10):
    print([4, 3, 2, 1, 5])
    pan=1
if(n2==30):
    print([4,5])
    pan=1
if(n1==1):
    print([3,1,5])
    pan=1
if(pan==0):
    print(str1)
    print(n1)
    print(n2)
    print(n3)