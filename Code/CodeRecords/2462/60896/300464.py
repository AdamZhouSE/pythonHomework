def find(list1):
    if(list1[0]>list1[1]):
        return 0
    for i in range(1,len(list1)-1):
        if(list1[i]>list1[i-1] and list1[i]>list1[i+1]):
            return i
    return len(list1)-1



temp=input().split(',')
b=map(eval,temp)
list1=list(b)
print(find(list1))