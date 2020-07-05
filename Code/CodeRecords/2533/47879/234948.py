a=input()
a=a[1:len(a)-1]
b=a.split(',')
list1=[]
for i in range(len(b)):
    list1.append(int(b[i]))
final_list=[]
for i in range(len(list1)):
    final_list.append(1)
j=0
k=len(list1)
for i in list1:
    if i%2==0:
        final_list[j]=i
        j=j+1
    else:
        final_list[k-1]=i
        k=k-1
print(final_list)