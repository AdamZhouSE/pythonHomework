n=int(input())
stair=[int(i) for i in input().split()]
re=[]
for i in range(1,n):
    if stair[i]==1:
        re.append(stair[i-1])
re.append(stair[n-1])
re=[str(i) for i in re]
print(str(len(re)))
print(" ".join(re))