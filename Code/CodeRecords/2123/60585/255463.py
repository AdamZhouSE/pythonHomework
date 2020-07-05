n=eval(input())
i=1
sum=0
isC=False
while sum<n:
    sum+=i
    i+=2
    if n==sum:
        isC=True
        break
print(isC)