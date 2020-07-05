num=int(input())
count=0
if num==1:
    count=0
else:
    for i in range(2,num+1):
        a=0
        for j in range(2,i):
            if i%j==0:
               a=1
        if  a==0:
            count=count+1
print(count)