a=input()
a=a[1:len(a)-1]
b=a.split(',')
list1=[]
for i in range(len(b)):
    list1.append(int(b[i]))
list1.sort()
print(list1)