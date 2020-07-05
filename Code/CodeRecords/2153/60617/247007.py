def main():
    Num=input()
    if Num[0]=="-":
        Num="-"+Num[1:][::-1]
        while Num[1]=="0":
            Num="-"+Num[1:]
    else:
        Num=Num[::-1]
        while Num[0]=="0":
            Num=Num[1:]
    print(Num)
    
if __name__=='__main__':
    main()