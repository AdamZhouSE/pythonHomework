paixushu=int(input().split(' ')[1])
a=input()
b=a.split(' ')
for i in range(0,len(b)):
    b[i]=int(b[i])
for i in range(0,paixushu):
    temp=input().split(' ')
    islow=int(temp[0])
    qi=int(temp[1])
    zhong=int(temp[2])
    temp=b[qi-1:zhong]
    temp.sort()
    if islow==1:
        temp.reverse()
    b=b[0:qi-1]+temp+b[zhong:len(b)]
index=int(input())
print(b[index-1])
