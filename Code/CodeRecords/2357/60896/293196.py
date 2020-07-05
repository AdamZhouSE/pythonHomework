a=eval(input())    
for i in range(0,a):
    temp=input().split(' ')
    b=map(eval,temp)
    list1=list(b)
    X=list1[2]
    temp=input().split(' ')
    b=map(eval,temp)
    list1=list(b)
    temp=input().split(' ')
    b=map(eval,temp)
    list2=list(b)
    result=[]
    for i in list1:
        for j in list2:
            if(i+j==X):
                result.append(i)
                result.append(j)
    if(len(result)==0):
        print(-1)
    else:
        for u in range(0,int(len(result)/2)):
            print(result[2*u],result[2*u+1])