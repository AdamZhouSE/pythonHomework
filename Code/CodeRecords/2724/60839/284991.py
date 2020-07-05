def opposite(x):
    return 7-x

n=int(input())
ans=[]
for i in range(0,n):
    x=int(input())
    ans.append(opposite(x))

for i in ans:
    print(i)