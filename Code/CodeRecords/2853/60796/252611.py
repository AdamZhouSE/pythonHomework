n=int(input())
ls=input().split(" ")
ls[int(x) for x in ls]
result=0
total=0
for i in range(n):
    total=total+ls[i]
for i in range(n):
    if (total-ls[i])%2==0:
        result=result+1
print(result)
    