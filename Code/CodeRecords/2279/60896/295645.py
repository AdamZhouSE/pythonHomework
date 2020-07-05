def find(list1,x):
    for i in range(0,len(list1)):
        count=0
        n=i
        result=[]
        while(count<x):
            if(n>=len(list1)):
                return([-1])
            count+=list1[n]
            n+=1
        if(count==x):
            result.append(i+1)
            result.append(n)
            return result
    
a=eval(input())
for i in range(0,a):
    temp=input().split(' ')
    b=map(eval,temp)
    list1=list(b)
    n=list1[0]
    x=list1[1]
    temp=input().split(' ')
    b=map(eval,temp)
    list1=list(b)
    result=find(list1,x)
    if(result==[-1]):print(-1)
    else:
        print(result[0],result[1])