def two(n:int)->int:
    temp=1
    for index in range (0,n):
        temp*=2
    return temp

def qufan(n:int)->int:
    shuzu=[]
    for index in range(0,32):
        shuzu.append(0)
    index=0
    while n>=1:
        shuzu[index]+=(n%2)
        index+=1
        n=(int)(n/2)
    temp=0
    for index1 in range(len(shuzu)):
        temp+=(1-shuzu[index1])*two(index1)
    return temp

n=(int)(input())
for index in range(0,n):
    x=(int)(input())
    print(qufan(x))
