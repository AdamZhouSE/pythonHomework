import math

def func(x,y):
    count=0
    for i in x:
        for j in y:
            if math.pow(i,j)>math.pow(j,i):
                count+=1
    return count

n=int(input())
ans=[]
for i in range(0,n):
    input()
    x = list(map(int, input().split(" ")))
    y = list(map(int, input().split(" ")))

    ans.append(func(x,y))
for i in ans:
    print(i)