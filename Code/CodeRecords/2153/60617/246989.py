def main():
    Num=input()
    if Num[0]=="-":
        print("-"+Num[1:][::-1])
    else:
        print(Num[::-1])

if __name__=='__main__':
    main()