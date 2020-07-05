import itertools
numbers=list(map(int,input()[1:-1].split(",")))
low=int(input())
up=int(input())
count=0
for p in itertools.combinations_with_replacement(range(0,len(numbers)),2):
    sum=0
    p1=p[0]
    p2=p[1]
    for i in range(p1,p2+1):
        sum=sum+numbers[i]
    if sum>=low and sum<=up:
        count=count+1
print(count)