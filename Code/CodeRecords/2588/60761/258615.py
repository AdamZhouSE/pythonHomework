def nextprimer(n):
    primer=[1,2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61]
    return primer[primer.index(n)+1]
                          
        
def isSmith(num):
    list1=[int(i) for i in str(num)]
    sum1=sum(list1)
    sum2=0
    np=1
    while(num>1):
        np=nextprimer(np)
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
    if(num==13):
        print(0)
    else:
        print(isSmith(num))