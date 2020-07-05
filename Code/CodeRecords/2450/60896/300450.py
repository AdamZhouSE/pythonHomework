def find(list1,c):
    if(not c in list1):
        return([-1,-1])
    else:
        x=(list1.index(c))
        for i in range(x+1,len(list1)):
            if(list1[i]!=c):
                return[x,i-1]
        return[x,len(list1)-1]

temp=input().split(',')
b=map(eval,temp)
list1=list(b)
c=eval(input())
print(find(list1,c))