def atoi():
    string=input()
    while string[0]==" ":
        string=string[1:]
    first=string[0]
    validFirst=["+", "-", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    if first not in validFirst:
        print(0)
        exit()
    num=first
    string=string[1:]
    for number in string:
        if number.isdigit():
            num+=number
        else:
            break
    num=int(num)
    if num>pow(2,31)-1:
        print(int(pow(2, 31)-1))
        exit()
    elif num<-int(pow(2, 31)):
        print(-int(pow(2, 31)))
        exit()
    print(num)

if __name__=='__main__':
    atoi()