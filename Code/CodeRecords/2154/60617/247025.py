def main():
    num=input()
    if num[0:]==num[::-1]:
        print(True)
    else:
        print(False)

if __name__=='__main__':
    main()