n=input()
n=int(n)
ls=input().split(" ")
ls=[int(ls[i]) for i in range(n)]
day=0
for i in range(n):
    if ls[i]==i+1:
        day=day+1
print(day)