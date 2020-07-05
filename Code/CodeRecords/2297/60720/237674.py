size=int(input())
list=input().split()
layer=int(input())
s=0
e=0
if layer==0:
    print('EMPTY')
else:
    for i in range(layer-1):
        s+=pow(2,i)
        e=s+pow(2,i+1)
    if e==0:
        e=1
    if s>size-1:
        print('EMPTY')
    else:
        if(e-1>size-1):
            for i in range(s,size-1):
                print(list[i],end=' ')
            print(list[size-1])
        else:
            for i in range(s,e-1):
                print(list[i],end=' ')
            print(list[e-1])