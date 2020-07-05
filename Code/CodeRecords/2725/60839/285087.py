def func(x):
    if x%2==0:
        return 1
    else:
        return 0


n=int(input())
ans=[]
for i in range(0,n):
    x=int(input())
    ans.append(func(x))

for i in ans:
    print(i)