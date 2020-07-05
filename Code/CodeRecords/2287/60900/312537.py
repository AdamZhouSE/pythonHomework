n = int(input())
str = []
for i in range(0,n):
    a = input()
    str.append(input().split(' '))
    for j in range(0,len(str[i])):
        str[i][j]=int(str[i][j])


for i in range(0,n):
    nums =str[i]
    l = len(str[i])
    temp =-1
    for j in range(0,l):
        temp=-1
        for m in range(j+1,l):
            if nums[m]>=nums[j]:
                temp=nums[m]
                break
        if j !=l-1:
            print(temp,end=' ')
        else:
            print(temp)