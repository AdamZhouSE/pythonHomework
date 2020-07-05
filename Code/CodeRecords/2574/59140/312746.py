t = int(input())
res=[]
for i in range(2,1000):
    flag=True
    for j in range(2,i):
        if i%j==0:flag=False
    if flag:res.append(i)
for _ in range(t):
    n = int(input())
    print(pow(res[n-1],2)+1)