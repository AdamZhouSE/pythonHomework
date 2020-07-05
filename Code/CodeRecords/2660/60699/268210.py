n=int(input())
list1=""
for i in range(n):
    str=input().split(' ')
    if str[0]=='T':
        list1=list1+str[1]
    elif str[0]=='U':
        x=int(str[1])
        list1=list1[0:(len(list1)-x)]
    elif str[0]=='Q':
        print(list1[int(str[1])-1])