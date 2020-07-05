num=int(input())
numbers=list(map(int,input().split(" ")))
numbers.sort()
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
    countO=countO-countH
    countH=0
    
if countT==0:
    count=count+countO//4
    countO=countO%4
    if countO!=0:
        count=count+1
else:
    count=count+1
    if countO>=2:
        countO=countO-2
    count = count + countO // 4
    countO = countO % 4
    if countO != 0:
        count = count + 1
print(count)