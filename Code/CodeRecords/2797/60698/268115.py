#37
def test():
    n=int(input())
    arr=input().split()
    arr=list(map(int,arr))
    if n==1:
        if arr[0]==15:
            print('DOWN')
            return
        elif arr[0]==0:
            print('UP')
        else:
            print(-1)
        return
    else:
        if arr[-1]==15:
            print('DOWN')
            return
        elif arr[-1]==0:
            print('UP')
            return
        else:
            if arr[-1]-arr[-2]>0:
                print('UP')
                return
            else:
                print('DOWN')
                return

test()