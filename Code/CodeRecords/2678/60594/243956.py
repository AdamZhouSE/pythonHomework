
def qufan(n:int):
    shuzu=[]
    while n>=1:
        shuzu.append(n%2)
        n=(int)(n/2)
    count=0
    temp=0
    for index in range(len(shuzu)):
        if shuzu[index]==1:
            count+=1
        temp=index
    if count>1:
        print(-1)
    else:
        print(temp+1)

n=(int)(input())
for index in range(0,n):
    x=(int)(input())
    qufan(x)