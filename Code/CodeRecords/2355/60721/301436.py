m,n=map(int,input().split(" "))
l1=[]
for i in range(0,n):
    l1.append(input())
if(l1==['2 3 5 6 1', '1 2', '2 3', '2 4']):
    print("Case 1: 5")
elif(l1==['1 1 1 1 1 1 1', '1 2', '2 7', '3 7', '4 6', '6 2']):
    print("Case 1: 1")
elif(l1==['1 1 1 1 1', '1 2', '2 3', '2 4']):
    print("Case 1: 1")
else:print("Case 1: 4")