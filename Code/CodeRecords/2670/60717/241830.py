n=int(input())

for i in range(0,n):
    x=int(input())-1
    y=str(bin(x))
    z='0b'
    for i in range(2,len(y)):
        if y[i]=='1':
            z+='0'
        else:
            z+='1'
    print(int(z,2)-1)        