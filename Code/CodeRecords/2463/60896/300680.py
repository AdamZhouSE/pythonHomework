def find(list1,c):
    result=[]
    for i in range(len(list1)-1):
        x=list1[i]
        for j in range(i+1,len(list1)):
            y=list1[j]
            if(y>c):
                break
            if(x+y==c):
                result.append(i+1)
                result.append(j+1)
                return result

temp=input().split(',')
b=map(eval,temp)
list1=list(b)
c=eval(input())
print(find(list1,c))
            