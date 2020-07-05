num=eval(input())
lower=int(input())
upper=int(input())
count=0
for i in num:
    if i>=lower and i<=upper:
        count+=1
print(count)