def find(list1):
    up=True
    result=0
    count=1
    for i in range(1,len(list1)):
        if(list1[i]>list1[i-1]):
            count+=1
        else:
            result=max(count,result)
            count=0
    return result

a=input()
a=a[1:len(a)-1]
temp=a.split(',')
b=map(eval,temp)
list1=list(b)
print(find(list1))