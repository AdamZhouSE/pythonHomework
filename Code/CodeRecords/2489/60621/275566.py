a=eval(input())
lower=eval(input())
upper=eval(input())
sum=0
for i in range(len(a)):
    total=0
    j=i
    while j<len(a):
        total+=a[j]
        if lower<=total and upper>=total:
            sum+=1
        j+=1
print(sum)