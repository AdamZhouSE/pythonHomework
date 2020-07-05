def func(x):
    ans=0
    for i in range(1,x+1):
       ans=ans+i*i
    return ans

n=int(input())
ans=[]
for i in range(0,n):
    ans.append(func(int(input())))

for i in ans:
    print(i)