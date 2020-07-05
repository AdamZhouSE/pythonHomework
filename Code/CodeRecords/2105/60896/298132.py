temp=input().split(',')
b=map(eval,temp)
list1=list(b)
result=(list1[2]-list1[0])*(list1[3]-list1[1])+(list1[6]-list1[4])*(list1[7]-list1[5])
if(list1[2]<=list1[4] or list1[3]<=list1[5] or list1[0]>=list1[6] or list1[1]>=list1[7]):
    print(result)
x=[]
y=[]
for i in range(0,7,2):
    x.append(list1[i])
for i in range(1,8,2):
    y.append(list1[i])
x.sort()
y.sort()
common=(x[2]-x[1])*(y[2]-y[1])
print(result-common)
    