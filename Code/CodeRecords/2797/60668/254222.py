def arrays_37_Moon(list = []):
    n = len(list)
    if n>1:
        if list[n-2]>list[n-1] and (not(list[n-1] == 0)):
            print("DOWN")
        else:
            print("UP")
    else:
        print(-1)
if __name__=='__main__':
    n = input()
    list = [int(i) for i in input().split()]
    arrays_37_Moon(list)