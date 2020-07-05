def findSame(a,b,leng):
    result=0
    for Astart in range(len(a)-leng+1):
        for Bstart in range(len(b)-leng+1):
            if a[Astart:Astart+leng]==b[Bstart:Bstart+leng]:
                result+=1
    return result

a=str(input())
b=str(input())
num=0
for i in range(1,len(a)):
    res=findSame(a,b,i)
    num+=res
    if res==0:
        break
print(num,end='')
