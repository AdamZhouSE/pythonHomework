num=int(input())
res=''
num=int(input())
res=''
count=0
if num==0:
    res=0
while(num):
    s=num%2
    res+=str(int(s))
    if 1 == count % 2:
        num += s
    num //= 2
    count += 1
res = list(res)
res.reverse()
print("".join(res))
if num==0:
    res=0
while(num):
    s=num%(-2)
    num=num/2
    if s<0:
        s+=2
        num+=1
    res=str(s)+res
print(res)