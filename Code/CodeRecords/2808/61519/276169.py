n=int(input())
num=list(input().split(" "))
poss=[]
for i in range(n):
    num[i]=int(num[i])
min=num.index(min(num))+1
max=num.index(max(num))+1
poss.append(n-min)
poss.append(min-1)
poss.append(max-1)
poss.append(n-max)
poss.sort(reverse=True)
print(poss[0])