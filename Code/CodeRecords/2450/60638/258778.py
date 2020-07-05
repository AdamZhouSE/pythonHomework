numbers=list(map(int,input().split(",")))
num=int(input())
begin=0
end=len(numbers)
res=[]
i=(begin+end)//2
find=False
while begin!=end:
    if num==numbers[i]:
        find=True
        break
    if num<numbers[i]:
        end=i
    else:
        begin=i
    i=(begin+end)//2
    if end==begin+1:
        break
if find:
    k=i
    while numbers[i]==num:
        i=i-1
    res.append(i+1)
    i=k
    while numbers[i]==num:
        i=i+1
    res.append(i-1)
    print(res)
else:
    res.append(-1)
    res.append(-1)
    print(res)