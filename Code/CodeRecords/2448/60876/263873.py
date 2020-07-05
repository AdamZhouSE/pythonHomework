nums=eval(input())
h=0
sum=1
while sum>h:
    h+=1
    sum=0
    for item in nums:
        if item>h:
            sum+=1
print(h)