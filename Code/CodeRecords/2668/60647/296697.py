n=int(input())
for i in range(n):
    b=int(input())
    strr=bin(b).replace('0b','')
    strrr='0b'
    for i in strr:
        if i=='0':
            strrr+='1'
        else:
            strrr+=i
    a=int(strrr,2)
    print(a-b,end=' ')
    print(a)