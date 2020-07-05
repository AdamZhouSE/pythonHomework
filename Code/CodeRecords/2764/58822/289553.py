def com(n):
    li=[]
    sum=0
    if(n<12):
        return n
    li.append(int(n/2))
    li.append(int(n / 3))
    li.append(int(n / 4))
    for i in range(0,len(li)):
        sum=sum+com(li[i])
    return sum
num=int(input())
for i in range(num):
    n=int(input())
    sum=0
    print(com(n))