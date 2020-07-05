n=int(input())
res=1
num=0
for i in range(1,int(n/2)+2):
    for j in range(i,int(n/2)+2):
        num=j+num
        if num==n:
            res+=1
            num=0
            break
        if num>n:
            num=0
            break
print(res)