def linerlist_shoot(X,Y,Z):
    xz = Z
    yz = Z
    co_x = 0
    co_y = 0
    while xz!=1:
        if X%xz==0:
            X-=1
            xz-=1
            co_x+=1
        else:
            xz-=1
    while yz!=1:
        if Y%yz ==0:
            Y-=1
            yz-=1
            co_y+=1
        else:
            yz-=1
    print(co_x,end=' ')
    print(co_y,end='\n')
if __name__=='__main__':
    for _ in range(int(input())):
        X,Y,Z=input().split()
        linerlist_shoot(int(X),int(Y),int(Z))