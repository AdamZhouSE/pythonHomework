def main():
    num=int(input())
    half=num//2
    for i in range(0, half+1):
        for j in range(0, half+1):
            if (i+j)**2==num:
                print(True)
                exit()
    print(False)

if __name__=='__main__':
    main()