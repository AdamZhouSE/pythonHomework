def isspe(a):
    if(a==1):
        return False
    for i in range(2,a):
        if(a%i==0):
            return False
    return True



testnum=int(input())
for i in range(testnum):
    count=0
    num=int(input())
    for m in range(2,num):
        if((num%m==0)&(isspe(m))):
            num=int(num/m)
            count+=1
            if(count==3):
                break
            else:
                continue
    if(count<3):
        print(0)
    else:
        if(num!=1):
            print(0)
        else:
            print(1)