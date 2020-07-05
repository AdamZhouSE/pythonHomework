temp=[int(x) for x in input().split(',')]

for i in range(len(temp)):
    print(temp[i],end='')
    if(i!=len(temp)-1):
        print('/',end='')
    else:
        print(')')
    if(i==0):
        print('(',end='')
    