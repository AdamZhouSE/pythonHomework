a=int(input())
b=input().split()
b=[int(x)for x in b]
b=sorted(b)
summ=0
for i in b:
    summ+=i
print(b[-1]*a-summ)