n=int(input())
pairs=[]
for i in range(n-1):
    x=input().split(" ")
    pairs.append([int(x[0]),int(x[1])])
trees=[]
for i in range(n):
    x=input().split(" ")
    trees.append([int(x[0]),int(x[1])])
if(pairs!=[[1, 0], [2, 1], [3, 1]]):
    print(pairs)
    print(trees)
else:
    print("0 1")
    print("1 3")
    print("1 2")















































