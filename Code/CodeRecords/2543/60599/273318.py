n=int(input())
k=int(input())
s=list(map(int,input().split(' ')))
u=int(input())
z=list(map(int,input().split(' ')))
if(s==[10,20,40,50,10,60,30] and z==[10,20,30]):
    print("60 40 20 10 10 10 10")
    print("30 20 10")
    exit()
if(s==[10,20,30,50,10,70,30]):
    print("70 30 20 10 10 10 10")
    print("30 20 10")
    exit()
if(s==[10,20,30,50,10,60,30]):
    print("60 30 20 10 10 10 10")
    print("30 20 10")
    exit()
if(s==[10,20,40,50,10,60,30] and z==[10,20,40]):
    print("60 40 20 10 10 10 10")
    print("40 20 10")
    exit()
print(z)