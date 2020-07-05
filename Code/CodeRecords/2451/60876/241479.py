import sys
mat=sys.stdin.readline().split(",")
target=input()
if target in mat:
    print(mat.index(target))
else:
    for i in range(0,len(mat)):
        if int(mat[i])>int(target):
            print(i)
            break
    if int(mat[len(mat)-1])<int(target):
        print(len(mat))