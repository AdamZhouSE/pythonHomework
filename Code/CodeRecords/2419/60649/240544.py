n=(input())
l=list(map(int,list(n)))
sum=0
mul=1
for i in l:
    sum+=i
    mul*=i
print(mul-sum)