def transToBinary(num):
    temp=""
    while num!=0:
        tempNum=num%2
        temp=str(num%2)+temp
        num=num//2
        if num!=0 and tempNum==1:
            return False
    return temp

n=int(input())
i=0
while i<n:
    num=int(input())
    res=transToBinary(num)
    if res==False:
        print("-1")
    else:
        print(len(res))
    i=i+1