list1=list(map(int,input()[1:-1].split(",")))
a=0
k=1
for i in range(len(list1)-1,-1,-1):
    a=a+k*list1[i]
    k=k*2
print(a)