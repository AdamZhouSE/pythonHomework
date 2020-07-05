list1=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
n=int(input())
for i in range(0,n):
    x=int(input())
    list2=[]
    while not(x in list1):
        for i in list1:
            if x%i==0:
                list2.append(i)
                x=int(x/i)
                break
    list2.append(x)
    summ=''
    for i in list2:
        summ+=str(i)
    list3=list(str(n))
    list4=list(summ)
    sum1=0
    for i in list3:
        sum1+=int(i)
    sum2=0
    for i in list4:
        sum2+=int(i)
    if sum1==sum2:
        print(1)
    else:
        print(0)
        
        
        
        
        
        
        
        
        
        