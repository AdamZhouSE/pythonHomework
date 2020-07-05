def find_black(arr,r,c):
    up,down,left,right=0,0,0,0
    find=False
    for i in range(r):
        if find:
            if 'B' not in arr[i]:
                down=i-1
                break
        else:
            for j in range(c):
                if arr[i][j]=='B':
                    up=i
                    left=j
                    find=True
                    for x in range(j+1,c):
                        if arr[i][x]=='W':
                            right=x-1
                            break
                    break
    print((up+down)//2+1,(left+right)//2+1)

r_c=input().split()
r,c=int(r_c[0]),int(r_c[1])
arr=[]
for i in range(r):
    row=input()
    arr.append(list(row))
find_black(arr,r,c)