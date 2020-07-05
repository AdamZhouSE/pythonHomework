n=int(input())
for i in range(n):
    a=int(input())
    strr1=bin(a).replace('0b','')
    strr=''
    for j in range(8-len(strr1)):
        strr+='0'
    strr+=strr1
    strrr='0b'
    for i in range(0,len(strr),2):
        if i+1 <len(strr):
            strrr+=strr[i+1]
        strrr+=strr[i]
    b=int(strrr,2)
    print(b)