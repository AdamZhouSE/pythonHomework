numbers=list(map(int,input()[1:-1].split(",")))
numbers.sort()
h=1
for i in range(1,len(numbers)+1):
    count=0
    for j in range(0,len(numbers)):
        if numbers[j]>=i:
            count+=1

    if i==count:
        h=i
        break
if numbers[0]!=1 and h==1:
    print(2)
else:
    print(h)

