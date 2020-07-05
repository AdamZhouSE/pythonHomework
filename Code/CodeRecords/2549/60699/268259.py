list1=list(map(int,input().split(' ')))
n=list1[1]
values=list(map(int,input().split(' ')))
values.sort(reverse=True)
for i in range(n):
    temp=list(map(int,input().split(' ')))
    if temp[0]==1:
        print(values[temp[1]-1])
    else:
        values.append(temp[1])
        values.sort(reverse=True)