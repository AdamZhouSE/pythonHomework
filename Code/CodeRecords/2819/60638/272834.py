num=int(input())
numbers=list(map(int,input().split(" ")))
numbers.sort()
begin=0
end=len(numbers)
count=0
countO=0
countT=0
countH=0
countF=0
for n in numbers:
    if n==1:
        countO=countO+1
    elif n==2:
        countT=countT+1
    elif n==3:
        countH=countH+1
    else:
        countF=countF+1
count=count+countF
count=count+countT//2
countT=countT%2
count=count+countH
if countH>countO:
    countH=countH-countO
    countO=0
else:
    countH=0
    countO=countO-countH
if countT==1:
    if countO<=2:
        count=count+1
    else:
        countO=countO-2
        count=count+1
count=count+countO//4
countO=countO%4
if countO==0:
    print(count)
else:
    print(count+1)