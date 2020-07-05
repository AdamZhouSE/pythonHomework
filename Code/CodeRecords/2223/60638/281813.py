line=input().split(",")
numbers= [int(n) for n in line]
numbers.sort()
i=0
a=0
b=0
res=[]
while i<len(numbers)-1:
    if numbers[i+1]-numbers[i]!=1:
        if numbers[i+1]-numbers[i]==2:
            b=numbers[i]+1
        else:
            a=numbers[i]
    i=i+1
if b==0:
    if numbers[0]!=1:
        b=1
    elif numbers[len(numbers)-1]==numbers[len(numbers)-2]:
        b=numbers[len(numbers)-1]+1
res.append(a)
res.append(b)
print(res)