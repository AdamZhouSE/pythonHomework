def rev_num():
    num=input()
    if num == '0':
        print("0")
        return
    if num[0]=='-':
        temp=num[1:][::-1]
        while temp[0]=='0':
            temp=temp[1:]
        print('-'+temp,end="")
    else:
        temp=num[::-1]
        while temp[0]=='0':
            temp=temp[1:]
            print(temp,end="")

if __name__=='__main__':
    rev_num()