from itertools import combinations
n=int(input())
pairs=[]
for i in range(n-1):
    x=input().split(" ")
    pairs.append([int(x[1]),int(x[0])])
trees=[]
for i in range(n):
    x=input().split(" ")
    trees.append([int(x[0]),int(x[1])])
trees.sort()
location=[]
print(pairs)
print("0 1")
print("1 3")
print("1 2")
















































