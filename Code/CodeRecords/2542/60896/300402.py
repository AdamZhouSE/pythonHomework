a=input()
a=a[1:len(a)-1]
temp=a.split(',')
b=map(eval,temp)
list1=list(b)
list1.sort()
count=1
result=0
for i in range(1,len(list1)):
    if(list1[i]==list1[i-1]+1):
        count+=1
    else:
        result=max(result,count)
        count=1
print(result)