n=int(input())
num=list(input().split(" "))
poss=[]
for i in range(n):
    num[i]=int(num[i])
min=num.index(min(num))
max=num.index(max(num))
poss.append(n-min-1)
poss.append(min-1)
poss.append(max-1)
poss.append(n-max-1)
poss.sort(reverse=True)
print(poss[0])