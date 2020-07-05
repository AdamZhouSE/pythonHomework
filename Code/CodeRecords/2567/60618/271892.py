num=[int(n) for n in input().split(",")]
lower=int(input())
upper=int(input())
count=0
for i in num:
    if i>=lower and i<=upper:
        count+=1
print(count)