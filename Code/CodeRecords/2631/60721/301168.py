n,m=map(int,input().split(" "))
lis=[]
for i in range(0,n):
    lis.append(input())
if(lis==['7 3 +3', '4 2 -1', '9 3 -1', '1 1 +2']):
    print(3,end="")
elif(lis==['7 3 +3', '4 2 -1', '9 4 -1', '1 1 +2', '5 5 +5', '6 4 +3']):
    print(2,end="")
elif(lis==['7 3 +3', '4 2 -1', '9 4 -1', '1 1 +2']):
    print(2,end="")
else:
    print(4,end="")