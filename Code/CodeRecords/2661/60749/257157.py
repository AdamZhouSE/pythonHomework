n=int(input())
res=[]
for _ in range(n):
    res.append(int(input()))
def twobinary(num):
    res=""
    while num>0:
        res=str(num%2)+res
        num=num//2
    return res
def count_one_and_two(num):
    res=twobinary(num)
    count1=0
    count0=0
    for h in res:
        if h=="1":
            count1+=1
        else:
            count0+=1
    return count0,count1
for t in res:
    count0,count1=count_one_and_two(t)
    print(count0^count1)