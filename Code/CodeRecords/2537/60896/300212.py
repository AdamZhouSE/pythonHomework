a=input()
c=eval(input())
a=a[1:len(a)-1]
temp=a.split(',')
b=map(eval,temp)
list1=list(b)
list1.sort()
print(list1[len(list1)-c])