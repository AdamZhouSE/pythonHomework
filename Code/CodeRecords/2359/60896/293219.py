a=eval(input())    
for i in range(0,a):
    n=eval(input())
    temp=input().split(' ')
    b=map(eval,temp)
    list1=list(b)
    count=0
    for j in range(0,n-2):
        x=list1[j]
        for k in range(j+1,n-1):
            y=list1[k]
            for l in range(k+1,n):
                z=list1[l]
                if(x+y==z or x+z==y or y+z==x):
                    count+=1
    if(count==0):print(-1)
    else:print(count)