def main():
    target=int(input())
    MaxNum=3**100
    if target==0:
        print(False)
        exit()
    if MaxNum%target==0:
        print (True)
    else:
        print(False)

if __name__=='__main__':
    main()