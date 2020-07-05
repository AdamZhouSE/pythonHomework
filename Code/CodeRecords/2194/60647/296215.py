n=int(input())
def panduan(n):
    if n==1:
        return False
    if n==2:
        return True
    else:
        for i in range(2,n-1):
            if n%i==0:
                return False
        return True
for i in range(n):
    list1=input().split()
    a=int(list1[0])
    b=int(list1[1])
    list=[]
    for j in range(a,b+1):
        if panduan(j):
            list.append(j)
    strr = ''
    for j in range(len(list) - 1):
        strr += str(list[j])
        strr += ' '
    print(strr, end='')
    print(list[-1], end='')
    print(' ')
