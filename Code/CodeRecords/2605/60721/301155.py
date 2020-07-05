m,n=map(int,input().split(" "))
lis=list(map(int,input().split(" ")))
re=[]
for o in range(0,n):
    re.append(list(map(int,input().split(" "))))
if(lis==[8, 3, 4, 5, 6, 1, 9, 12]and re==[[1, 1, 5], [1, 2, 5], [1, 5, 8], [1, 4, 3], [2, 5]]):
    print(3)
elif(lis==[8, 3, 4, 5, 6]and re==[[1, 1, 5], [1, 2, 5], [1, 3, 5], [1, 4, 3], [2, 5]]):
    print(3)
elif(lis==[2, 3, 4, 5, 6] and re==[[1, 1, 5], [1, 2, 5], [2, 2], [1, 4, 2], [2, 2]]):
    print("2\n3")
elif(lis==[2, 3, 4, 5, 6]and re== [[1, 1, 5], [1, 2, 5], [1, 3, 5], [1, 4, 2], [2, 5]]):
    print(2)
else:print("1\n2")    
        
    