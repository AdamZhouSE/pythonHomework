test = list(input())
sum=0
mul=1

for x in test:
    sum+=int(x)
    mul*=int(x)
print(mul-sum)
