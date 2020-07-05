def Test():
    n=int(input())
    mat=[]
    for i in range(0,n):
        mat.append(eval("["+input()+"]"))
    index=int(input())
    map=[]
    for i in range(0,n):
        for j in range(0,n):
            map.append(mat[i][j])
    map.sort()
    print(map[index-1])

if __name__ == "__main__":
    Test()
