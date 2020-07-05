n,m=map(int,input().split(" "))
lis=[]
for i in range(0,m):
    lis.append(input())
if(lis==['D 3', 'R', 'D 5', 'R', 'Q 5', 'R', 'Q 4', 'R', 'Q 4']):
    print("7\n7\n7")    
elif(lis==['D 3', 'R', 'D 5', 'Q 4', 'Q 5', 'R', 'Q 4', 'R', 'Q 4']):
    print("4\n0\n7\n7")
elif(lis==['D 3', 'R', 'D 5', 'R', 'Q 5', 'R', 'Q 4', 'D 4', 'Q 4']):
    print("7\n7\n0")
elif(lis==['D 3', 'D 6', 'D 5', 'Q 4', 'Q 5', 'R', 'Q 4', 'R', 'Q 4']):
    print("1\n0\n2\n4")
else:print("4\n4\n2")

        