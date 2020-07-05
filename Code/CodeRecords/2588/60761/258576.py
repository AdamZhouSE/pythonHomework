def nextprimer(n):
    if(n<3):
        return n+1
    j=n+2
    while(True):
        for i in range(2,int(j**0.5)+1):
            if(j%i==0):
                j=j+2
                i=2
            elif(i==int(j**0.5)-1):
                return j            
        
def isSmith(num):
    list1=[int(i) for i in str(num)]
    sum1=sum(list1)
    print(sum1)
    sum2=0
    np=1
    while(num>1):
        np=nextprimer(np)
        print(num,np)
        while(num%np==0):
            num=num/np
            sum2+=sum([int(i) for i in str(np)])
    if(sum1==sum2):
        return 1
    else:
        return 0

n=int(input())
for i in range(n):
    num=int(input())
    print(isSmith(num))