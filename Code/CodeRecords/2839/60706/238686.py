n=int(input())
str='NO'
list=[]
for i in range(0,n):
    list.append(input())
print('NO')
for i in range(1,n):
    j=i-1
    while j>=0:
        if list[i]==list[j]:
            str='YES'
        j=j-1
    print(str)
            