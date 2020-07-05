list1=input().split()
n=int(list1[0])
x0=int(list1[1])
y0=int(list1[2])
list1=[]
for i in range(0,n):
    list2=input().split()
    x1=int(list2[0])
    y1=int(list2[1])
    if x0==x1:
        list1.append('inf')
    else:
        list1.append(str('%.6f'%((y1-y0)/(x1-x0))))
print(len(list(set(list1))))