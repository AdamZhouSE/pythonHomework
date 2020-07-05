m,n=map(int,input().split())
num=[int(i) for i in input().split()]
re=[]
for i in range(0,n):
    a,b=map(int,input().split())
    mini=max(num)
    for j in range(a-1,b):
        if num[j]<mini:
            mini=num[j]
    re.append(mini)
re=[str(i) for i in re]
print(" ".join(re),end="")