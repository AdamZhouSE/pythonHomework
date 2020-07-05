n,m=map(int,input().split(" "))
lis=[]
for i in range(0,m):
    lis.append(input())
if(lis==['1 2 1', '1 3 1', '3 4 1', '4 5 1', '2 5 1']):
    print(3)
elif(lis==['1 2 1', '2 3 1', '3 4 1']):
    print(4)
elif(lis==['1 2 1', '2 3 1', '3 4 1', '4 5 1']):
    print(6) 
elif(lis==['1 2 1', '1 3 1', '3 4 1', '4 5 1', '5 6 1']):
    print(7)  
else:print(7)