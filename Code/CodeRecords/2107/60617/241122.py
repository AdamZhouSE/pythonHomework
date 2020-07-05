import sys
def main():
    Target=int(sys.stdin.readline())
    if Target == 1:
        print(True)
    elif Target % 2 != 0:
        print(False)
    else:
        while Target!=1:
            if Target % 2 != 0:
                print(False)
                exit()
            else:
                Target=Target/2
        print(True)
   
if __name__ == '__main__':
    main()