import sys
def main():
    sx=int(sys.stdin.readline())
    sy=int(sys.stdin.readline())
    tx=int(sys.stdin.readline())
    ty=int(sys.stdin.readline())

    def dfs(sx, sy, tx, ty):
        if sx==tx and sy==ty:
            print(True)
            exit()
        elif(sx<=tx and sy<=ty):
            dfs(sx+sy, sy, tx, ty)
            dfs(sx, sy+sx, tx, ty)

    if sx==tx and sy==ty:
        print(True)
    else:
        dfs(sx+sy, sy, tx, ty)
        dfs(sx, sy+sx, tx, ty)
    print(False)
if __name__ == '__main__':
    main()