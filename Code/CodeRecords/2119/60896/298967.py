def find(list1):
    for i in range(3,len(list1)):
        if(list1[i]>=list1[i-2] and list1[i-1]<=list1[i-3]):
            return True
    for i in range(4,len(list1)):
        if(list1[i]+list1[i-4]>=list1[i-2] and list[i-1]==list1[i-3]):
            return True
    for i in range(5,len(list1)):
        if(list1[i-3]>list1[i-5] and list1[i-2]>list1[i-4] and list1[i-1]<list1[i-3] and list1[i]>=list1[i-2]-list1[i-4]):
            return True
    return False

temp=input().split(',')
b=map(eval,temp)
list1=list(b)
print(find(list1))