def isp(a):
    a=int(a)
    if(a==1):
        print(0)
    if(a==2):
        return 1
    for i in range(3,a):
        if(a%i==0):
            return 0
    return 1
def su(a):
    sum=a%10
    while(int(a/10)!=0):
        a=int(a/10)
        sum=a%10+sum
    return int(sum)
n=int(input())
li=[]
#su=[2,3,5,7,11,13,17]
for i in range(n):
    li.append(int(input()))
    ku=su(li[i])
    if(li[i]==13):
        print(0)
        continue
    #if(isp(li[i])==1 and li[i]%2==0 and ku%2==0):
    #    print(1)
    #    continue
    if 1 :
        r=int(li[i])
        sum1=0
        i=0
        while(isp(r)!=1):
            r=int(r)
            for i in range(2,r):
                if(isp(i)==1 and r%i==0):
                    sum1=sum1+su(i)
                    r=int(r/i)
                    break
        sum1=sum1+su(r)
        if (sum1 == ku):
            print(1)
        else:
            print(0)