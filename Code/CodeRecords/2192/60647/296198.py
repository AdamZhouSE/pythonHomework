n=int(input())
for i in range(n):
    a=int(input())
    res=a
    list=[]
    list.append(a)
    while a>0:
        a=a-5
        list.append(a)
    while a!=res:
        a=a+5
        list.append(a)
    strr=''
    for j in range(len(list)-1):
        strr+=str(list[j])
        strr+=' '
    print(strr,end='')
    print(list[-1],end='')
    print(' ')