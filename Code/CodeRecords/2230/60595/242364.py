def Test():
    sx=int(input())
    sy = int(input())
    tx = int(input())
    ty = int(input())
    done=False
    while(tx>0 and ty>0):
        if(tx==sx and ty==sy):
            done=True
            break
        if(tx>ty):
            tx=tx-ty
        else:
            ty=ty-tx
    print(done)
if __name__ == "__main__":
    Test()