n=int(input())
res=[]
for _ in range(n):
    res.append(input().split(" "))
def twobinary(num):
    res=""
    while num>0:
        res=str(num%2)+res
        num=num//2
    return res
def comparetwobinary(num1,num2):
    if num1==num2:
        return -1
    num1str=twobinary(num1)
    num2str=twobinary(num2)
    if len(num1str)>len(num2str):
        while len(num1str)>len(num2str):
            num2str="0"+num2str
    elif len(num1str)<len(num2str):
        while len(num1str)<len(num2str):
            num1str="0"+num1str
    for t in range(len(num1str)-1,-1,-1):
        if not num1str[t]==num2str[t]:
            return len(num1str)-t
    return  -1
for h in res:
    print(comparetwobinary(int(h[0]),int(h[1])))