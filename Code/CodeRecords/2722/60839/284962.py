def func(x):
    if x%5==0:
        return "YES"
    else:
        return "NO"

n=int(input())
ans=[]

for i in range(0,n):
    ans.append(func(int(input())))

for i in ans:
    print(i)