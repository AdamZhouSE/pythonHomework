list1=list(map(int,input().split(' ')))
n=list1[1]
values=list(map(int,input().split(' ')))
for i in range(n):
    temp=list(map(int,input().split(' ')))
    list1=[]
    for j in range(temp[0]-1,temp[1]):
        list1.append(values[j])
    list1.sort()
    print(list1[temp[2]-1])