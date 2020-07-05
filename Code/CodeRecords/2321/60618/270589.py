d=[int(a) for a in input().split(',')]
n=int(input())

count=0
for i in range(1,n+1):
    length=len(list(str(i)))
    listi=list(str(i))
    re=1
    for j in range(0,length):
        if list[j] not in d:
            re=0
            break
    if re==1:
        count+=1
print(count)
        