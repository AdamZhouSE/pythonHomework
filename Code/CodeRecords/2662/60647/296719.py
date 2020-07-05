n=int(input())
for i in range(n):
    a=int(input())
    str1=bin(a)
    res=0
    for i in str1:
        if i=='1':
            res+=1
    if res%2==0:
        print('even')
    else:
        print('odd')