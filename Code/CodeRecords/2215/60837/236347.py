inp=input()
l=list(map(int,inp.split(',')))
if len(l)<=2:
    print(l[0],end='')
    if len(l)==2:
        print('/'+l[1])
else:
    for i in range(len(l)):
        if i==1:
            print('(',end='')
        if i==len(l)-1:
            print(str(l[i])+')')
        else:
            print(str(l[i])+'/',end='')
        
        
    