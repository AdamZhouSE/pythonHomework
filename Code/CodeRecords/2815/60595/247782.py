def Test():
    x=int(input())
    nums=eval("["+str(input()).strip().replace(" ",",")+"]")
    sum=0
    zheng=[]
    fu=[]
    zero=[]
    for num in nums:
        if(num>0):
            zheng.append(num)
        elif(num<0):
            fu.append(num)
        else:
            zero.append(num)
    zheng.sort()
    fu.sort()
    for a in zheng:
        sum=sum+a-1
    sum=sum+len(zero)
    if((len(fu)+len(zero))%2==0):
        for a in fu:
            sum=sum+(-1-a)
    else:
        small=max(fu)
        for a in fu:
            sum=sum+((-1-a) if a!=small else 1-a)
    print(sum)
if __name__ == "__main__":
    Test()