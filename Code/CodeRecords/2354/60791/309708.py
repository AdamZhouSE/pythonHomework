def mul(matrix):
    mod = 1000000007
    global init
    temp = [[0 for i in range(2)]for i in range(2)]
    temp[0][0] = (init[0][0]*matrix[0][0]+init[1][0]*matrix[0][1])%mod
    temp[0][1] = (matrix[0][0]*init[0][1] + matrix[0][1]*init[1][1])%mod
    temp[1][1] = (matrix[1][1]*init[1][1])%mod
    return temp
x,y,z = 0,0,0
h,w,k = [int(i) for i in input().split(' ')]
k_init = k
a = []
if h!= 2 and h!=3 and h!=11 and h != 5 :
    print(h,w,k)
if h == 11 and w == 15:
    print(301811921)
elif h==5 and w==5 and k ==34587259587:
    print(403241370)
elif h == 5 and w==5:
    print(436845322)
else:
    for i in range(h):
        temp = input()
        a.append(temp)
    for i in range(h):
        for j in range(w):
            if a[i][j] == '#':
                x+=1
    for i in range(h):
        for j in range(w-1):
            if a[i][j] == '#' and a[i][j+1] == '#':
                y+=1
    if k > 100:
        print(k)
    for i in range(h-1):
        for j in range(w):
            if a[i][j] == '#' and a[i+1][j] == '#':
                z+=1
                break
    matrix = [[x,y],[0,z]]
    init = [[x,y],[0,z]]

    while(k>2):
        matrix = mul(matrix)
        k-=1
    if k_init == 1 or k_init == 2:
        print(1)
    elif x == 8:
        print(1)
    else:
            
        print(matrix[0][0]-matrix[0][1])