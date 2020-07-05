size=int(input())
list1=[[]for i in range(size)]
for i in range(size):
    list2=input().split(',')
    for j in range(2):
        list2[j]=int(list2[j])
    list1[i]=list2
max=0
for x1 in range(size):
    for x2 in range(x1+1,size):
        for x3 in range(x2+1,size):
            s=abs((list1[x1][0]*list1[x2][1]+list1[x2][0]*list1[x3][1]+list1[x3][0]*list1[x1][1]-list1[x1][0]*list1[x3][1]-list1[x2][0]*list1[x1][1]-list1[x3][0]*list1[x2][1]) /2)
            if s>max:
                max=s
print(max)