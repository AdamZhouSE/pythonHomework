def qufan(a):
    strr=str(bin(a))[2:]
    while len(strr)<32:
        strr='0'+strr
    another='0b'
    for i in strr:
        if i =='1':
            another+='0'
        else:
            another+='1'
    return int(another,2)

n=int(input())

for i in range(0,n):
    print(qufan(int(input())))