n=int(input())
res=[]

def twobinary(num):
    res=""
    while num>0:
        res=str(num%2)+res
        num=num//2
    return res
for _ in range(n):
    res.append(int(input()))
def judge(num):
    count=0
    res=twobinary(num)
    for h in res:
        if h=="1":
            count+=1
    if count%2==1:
        return "odd"
    else:
        return "even"
for t in res:
    print(judge(t))