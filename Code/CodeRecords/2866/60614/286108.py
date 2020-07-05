length=int(input())
chocolates=[int(x) for x in input().split()]
result=1
judge=False
for i in chocolates:
    if i==1:
        if judge:
            result=result*count
            count=1
        else:
            judge=True
    else:
        count+=1
print(result)