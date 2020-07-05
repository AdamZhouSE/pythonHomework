def find(list1,x):
    for i in range(0,len(list1)-3):
        x1=list1[i]
        for m in range(i+1,len(list1)-2):
            x2=list1[m]
            for j in range(m+1,len(list1)-1):
                x3=list1[j]
                for k in range(j+1,len(list1)):
                    x4=list1[k]
                    if(x1+x2+x3+x4==x):
                        return True
    return False

a=eval(input())    
for i in range(0,a):
    n=eval(input())
    temp=input().split(' ')
    b=map(eval,temp)
    list1=list(b)
    x=eval(input())
    if(find(list1,x)):
        print(1)
    else:
        print(0)