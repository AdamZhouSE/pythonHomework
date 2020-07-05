temp=input().split(' ')
n=eval(temp[0])
m=eval(temp[1])
temp=input().split(' ')
b=map(eval,temp)
list1=list(b)
for i in range(m):
    temp = input().split(' ')
    b = map(eval,temp)
    list2 = list(b)
    rev=list2[0]
    index1= list2[1]
    index2=list2[2]
    if(rev==0):
        list3=sorted(list1[index1-1:index2])
    else:
        list3=sorted(list1[index1-1:index2],reverse=True)
    list1[index1-1:index2]=list3
a=eval(input())
print(list1[a-1])