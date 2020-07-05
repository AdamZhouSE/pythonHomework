n=int(input())
li=list(eval(input()))
re=0
for i in range(1,len(li)+1):
    for j in range(len(li)+1-i):
        sum=0
        for k in range(i):
            sum+=li[j+k]
        if sum>=n:
            re=i
            break
    if re!=0:
        break
print(re)
