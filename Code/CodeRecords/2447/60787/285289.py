m=int(input())
n=int(input())
num=[int(i) for i in input().split()]
re=[]
for i in range(0,n):
    a=int(input())
    b=int(input())
    mini=max(num)
    for j in range(a-1,b):
        if num[j]<mini:
            mini=num[j]
    re.append(mini)
re=[str(i) for i in re]
print(" ".join(re))