def find(list1,x):
    for i in range(0,len(list1)-1):
        for j in range(i+1,len(list1)):
            if(list1[i]*list1[j]==x):
                return True
    return False

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
    if(find(list1,x)):
        print('Yes')
    else:
        print('No')