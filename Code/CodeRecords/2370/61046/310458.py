
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