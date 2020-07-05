def rev_num():
    num=input()
    if num[0]=='-':
        temp=str(reversed(num[1:]))
        while temp[0]=='0':
            temp=temp[1:]
        print('-'+temp,end="")
    else:
        temp=str(reversed(num))
        while temp[0]=='0':
            temp=temp[1:]
            print(temp,end="")

if __name__=='__main__':
    rev_num()