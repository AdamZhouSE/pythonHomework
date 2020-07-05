def jue(a,b):
    min=abs(b[0]-a)
    for i in range(len(b)):
        k=abs(b[i]-a)
        if(k<min):
            min=k
    return min
num=int(input())
li=[]
sum=0
index=1
for i in range(num):
    k=int(input())
    li.append(k)
    if(len(li)==1):
        sum=li[0]
    if(len(li)>=2):
        sum=sum+jue(li[index],li[0:index])
        index+=1
print(sum,end='')