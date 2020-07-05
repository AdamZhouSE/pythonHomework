n=int(input())
num=input().split()
num=[int(x) for x in num]
answer=False
for i in range(n):
    if num[num[num[i]]]==i:
        answer==True
        print("YES")
        break
if not answer:
    print("NO")