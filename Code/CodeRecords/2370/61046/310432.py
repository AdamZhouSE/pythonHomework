num=int(input())
if num==0:
    ans=0
while(num):
    s=num%(-2)
    num=num/2
    if s<0:
        s+=2
        num+=1
    res=str(s)+res
print(res)