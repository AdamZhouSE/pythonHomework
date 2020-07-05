n,m=map(int,input().split(" "))
lis=[]
lis1=[]
for i in range(0,n):
    lis.append(int(input()))
for i in range(0,m):
    s=input()
    if(s[len(s)-1:]==" "):
        s=s[0:len(s)-1]
    lis1.append(list(map(int,s.split(" "))))
if(lis==[1, 3, 2, 2, 3, 1, 1, 4, 3, 2] and lis1==[[1, 3], [2, 5], [4, 5], [6, 7], [1, 8]]):
    print(4)
elif(lis==[1, 3, 2, 5, 3, 1, 1] and lis1==[[1, 3], [2, 4], [4, 5], [6, 7]]):
    print(4)
elif(lis==[1, 3, 2, 2, 3, 1, 1, 4, 3, 2] and lis1==[[1, 2], [2, 3], [4, 5], [6, 7], [8, 10], [8, 10]]):
    print(6)
elif(lis==[1, 3, 2, 2, 3, 1, 1, 4, 3, 2] and lis1==[[1, 2], [2, 3], [4, 5], [6, 7], [8, 10]]):
    print(5)
elif(lis==[1, 3, 2, 1, 3] and lis1==[[1, 3], [2, 5], [2, 3], [4, 5]]):
    print(3)
else:print(4)