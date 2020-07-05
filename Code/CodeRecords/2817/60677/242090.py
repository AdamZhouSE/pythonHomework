n=int(input())
num=input().split()
num=[int(x)-1 for x in num]
answer=False
for i in range(n):
    if num[num[num[i]]]==i:
        answer==True
        break
if not answer:
    print("NO")
else:
    print("YES")