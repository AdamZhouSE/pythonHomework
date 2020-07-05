def moon_Watcher():
    n=int(input())
    sizeOfMoon=list(map(int, input().split(" ")))
    if n==1:
        if sizeOfMoon[0]==15 or sizeOfMoon[0]==0:
            print("UP")
            exit()
    else:
        if sizeOfMoon[-2]>sizeOfMoon[-1]:
            if sizeOfMoon[-1]==0:
                print("UP")
                exit()
            else:
                print("DOWN")
                exit()
        else:
            if sizeOfMoon[-1]==15:
                print("DOWN")
                exit()
            else:
                print("UP")
                exit()

if __name__=='__main__':
    moon_Watcher()